from binance.client import Client
import pandas as pd
from datetime import datetime
from datetime import timedelta
from tqdm import tqdm

def calc_ticks(start, end, interval):
    """Tick calculator for tqdm progress bar

    Args:
        start (datetime): From date
        end (datetime): To date
        interval (str): Scale. '1m', '1h' or '1d'

    Returns:
        int: Total ticks for progress bar
    """
    if interval == '1m':
        return (end - start).total_seconds() / 60
    elif interval == '1h':
        return (end - start).total_seconds() / 3600
    elif interval == '1d':
        return (end - start).days
    else:
        return 1

def bloader(client, coin='BTCUSDT', interval='1h', start=datetime.utcnow()-timedelta(days=1), end=datetime.utcnow(), to_csv=False):
    """Downloader history data from binance

    Args:
        client ([type]): pytho-binance Client
        coin (str, optional): Ticker to dowload. Defaults to 'BTCUSDT'.
        interval (str, optional): '1m', '1h' or '1d'. Defaults to '1h'.
        start (datetime, optional): From date. Defaults to datetime.utcnow()-timedelta(days=1).
        end (datetime, optional): To date. Defaults to datetime.utcnow().
        to_csv (bool, optional): Save to csv file or not. Defaults to False.

    Returns:
        pd.DataFrame: History candles
    """
    df = pd.DataFrame()
    start_str = start.strftime('%Y-%m-%d %H:%M:%S')
    end_str = end.strftime('%Y-%m-%d %H:%M:%S')

    # set tqdm progress bar
    total = calc_ticks(start, end, interval)
    pbar = tqdm(total=total)

    # download data
    lines = []
    for kline in client.get_historical_klines_generator(coin, interval, start_str, end_str):
        lines.append(kline)
        pbar.update()
    pbar.close()

    # convert list of lists to dataframe
    df = pd.DataFrame(lines)
    df.columns=[
        'dateTime', 
        'open', 
        'high', 
        'low', 
        'close', 
        'volume', 
        'closeTime', 
        'quoteAssetVolume', 
        'numberOfTrades', 
        'takerBuyBaseVol', 
        'takerBuyQuoteVol', 
        'ignore']
    df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
    df.set_index('dateTime', inplace=True)

    # delete some columns
    df = df.drop([
            'closeTime', 
            'quoteAssetVolume', 
            'numberOfTrades', 
            'takerBuyBaseVol',
            'takerBuyQuoteVol', 
            'ignore'], 
        axis=1)
    
    # save to file
    if to_csv:
        filename = f'{coin}_{interval}.csv'
        df.to_csv(filename)
        print(f'saved to {filename}')

    return df

def main():
    client = Client('api key', 'api secret')
    coin = 'ETHUSDT'
    interval = '1m'
    start = datetime(2018, 1, 1)
    end = datetime(2019, 2, 1)
    
    candles = bloader(client, coin=coin, interval=interval, start=start, end=end, to_csv=True)
    print(candles)

if __name__ == '__main__':
    main()