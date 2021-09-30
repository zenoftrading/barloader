import os
import sys
import time
import random
import pandas as pd
import yfinance as yf
from loguru import logger
from tqdm.auto import tqdm
from datetime import datetime
from datetime import timedelta
from finam import Exporter, Market, Timeframe

# TODO
# disabling progress bar
# disabling logs
# directory by default
# other intervals: 5m, 15m, 4h
# update mode
# unit tests

class BarLoader:
    """Data history downloader from yahoofinance, finam and binance.
    """
    VALID_INTERVALS = ['1d', '1h']

    def __init__(self) -> None:
        self.start = datetime.utcnow()-timedelta(days=7)
        self.end = datetime.utcnow()
        self.interval = '1d'
        
        logger.add('barlodaer.log')
        logger.add(sys.stdout, level="ERROR")
    
    def yf(self, tickers, start=None, end=None, interval=None, tocsv=True, postfix=None):
        """Download history data from https://finance.yahoo.com/

        Args:
            tickers (list): list of tickers
            start (datetime, optional): Start date. Defaults to None (7 days ago).
            end (datetime, optional): End date. Defaults to None (now)
            interval (str, optional): Bar timeframe. Defaults to None (1d).
            tocsv (bool, optional): Save data to csv file or not. Defaults to True. 
                If False, data saved to list of dataframes.
            postfix (str, optional): Need for some tickers. For example, if you 
                need RUB/USD pair, ticker would be 'RUB' and postfix 'USD=X'. See ticker
                on yahoo finance. Defaults to None.

        Returns:
            list of dataframes: if tocsv=False array contains list of dataframes, 
                else list is empty
        """
        if postfix == None:
            postfix = ''

        if interval is None:
            interval = self.interval
            if interval not in self.VALID_INTERVALS:
                logger.error(f"Interval {interval} not valid. Available {', '.join(self.VALID_INTERVALS)}")
                return

        if start is None:
            start = self.start.strftime('%Y-%m-%d')
        elif interval == '1d':
            start = start.strftime('%Y-%m-%d')
        else:
            start = start.strftime('%Y-%m-%d %H:%M:%S')

        if end is None:
            end = self.end.strftime('%Y-%m-%d')
        elif interval == '1d':
            end = end.strftime('%Y-%m-%d')
        else:
            end = end.strftime('%Y-%m-%d %H:%M:%S')
        
        directory = self.interval            
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as e:
                logger.error(f"Directory \"{directory}\" creation error: {e}")
        
        tickers_list = []
        for ticker in tqdm(tickers):
            try:
                ticker = ticker + postfix
                human_filter = ''.join(filter(str.isalpha, ticker))
                logger.info(human_filter)
                df = yf.download(ticker, start=start, end=end, interval=interval, progress=False)
                if tocsv: 
                    df.to_csv(f".{os.sep}{directory}{os.sep}{human_filter}.csv")
                else:
                    tickers_list.append(df)
            except Exception as e:
                logger.error(f"Download {ticker} from yahoo finance error: {e}")
        
        return tickers_list

    
    def finam(self, tickers, market=None, start=None, end=None, interval=None, tocsv=True):
        """Download history data from https://www.finam.ru/

        Args:
            tickers (list): list of tickers
            start (datetime, optional): Start date. Defaults to None (7 days ago).
            end (datetime, optional): End date. Defaults to None (now)
            interval (str, optional): Bar timeframe. Defaults to None (1d).
            tocsv (bool, optional): Save data to csv file or not. Defaults to True. 
                If False, data saved to list of dataframes.
            market (str, optional): Need if you download futures. Defaults to None (shares).

        Returns:
            list of dataframes: if tocsv=False array contains list of dataframes, 
                else list is empty
        """
        if start is None:
            start = self.start
        else:
            start = datetime.strptime(start, '%Y-%m-%d').date()
        
        if end is None:
            end = self.end
        else:
            end = datetime.strptime(end, '%Y-%m-%d').date()

        if interval is None or interval == '1d':
            directory = '1d'
            interval = Timeframe.DAILY
        elif interval == '1h':
            directory = '1h'
            interval = Timeframe.HOURLY
        else:
            logger.error(f"Interval {interval} not valid")
            return

        if market == 'futures':
            market = Market.FUTURES_ARCHIVE
        else:
            market = Market.SHARES

        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as e:
                logger.error("Directory \"{directory}\" creation error: {e}")

        tickers_list = []
        exporter = Exporter()
        for ticker in tqdm(tickers):
            try:
                logger.info(ticker)
                asset = exporter.lookup(code=ticker, market=market)
                asset_id = asset[asset['code'] == ticker].index[0]
                df = exporter.download(asset_id, market=market, start_date=start, end_date=end, timeframe=interval, delay=random.randint(3,5))
                df['<DATE>'] = pd.to_datetime(df['<DATE>'], format='%Y%m%d')
                df.drop('<TIME>', axis=1, inplace=True)
                columns = {'<DATE>': 'Date', '<OPEN>': 'Open', '<HIGH>': 'High', '<LOW>': 'Low', '<CLOSE>': 'Close', '<VOL>': 'Volume'}
                df = df.rename(columns=columns).set_index('Date')
                if tocsv: 
                    df.to_csv(f".{os.sep}{directory}{os.sep}{ticker}.csv")
                else:
                    tickers_list.append(df)
                time.sleep(random.randint(3, 5))                
            except Exception as e:
                logger.error(f"Download {ticker} from finam error: {e}")
        
        return tickers_list

   
    def binance(self, tickers, client, start=None, end=None, interval=None, tocsv=True):
        """Download history data from https://www.binance.com

        Args:
            client (binance.client.Client class): binance api client https://github.com/sammchardy/python-binance
            tickers (list): list of tickers
            start (datetime, optional): Start date. Defaults to None (7 days ago).
            end (datetime, optional): End date. Defaults to None (now)
            interval (str, optional): Bar timeframe. Defaults to None (1d).
            tocsv (bool, optional): Save data to csv file or not. Defaults to True. 
                If False, data saved to list of dataframes.

        Returns:
            list of dataframes: if tocsv=False array contains list of dataframes, 
                else list is empty
        """
        if start == None:
            start = self.start.strftime('%Y-%m-%d %H:%M:%S')
        else:
            start = start.strftime('%Y-%m-%d %H:%M:%S')
                
        if end == None:
            end = self.end.strftime('%Y-%m-%d %H:%M:%S')
        else:
            end = end.strftime('%Y-%m-%d %H:%M:%S')

        if interval == None:
            interval = self.interval
            if interval not in self.VALID_INTERVALS:
                logger.error(f"Interval {interval} not valid")
                return            

        directory = interval        
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except Exception as e:
                logger.error("Directory \"{directory}\" creation error: {e}")

        # download data
        tickers_list = []
        for ticker in tqdm(tickers):
            try:
                logger.info(ticker)
                df = pd.DataFrame()
                lines = []
                for kline in client.get_historical_klines_generator(ticker, interval, start, end):
                    lines.append(kline)
                
                # convert list of lists to dataframe
                df = pd.DataFrame(lines)
                df.columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 
                    'closeTime', 'quoteAssetVolume', 'numberOfTrades', 
                    'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore']
                df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')
                df.set_index('dateTime', inplace=True)
                
                # delete some unuseful columns
                df = df.drop(['closeTime', 'quoteAssetVolume', 'numberOfTrades', 
                    'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)
                
                # save to file
                if tocsv:
                    df.to_csv(f".{os.sep}{directory}{os.sep}{ticker}.csv")
                else:
                    tickers_list.append(df)
            except Exception as e:
                logger.error(f"Download {ticker} from binance error: {e}")
        
        return tickers_list
    
if __name__ == '__main__':
    # usage examples
    bl = BarLoader()

    # finam shares    
    f = bl.finam(['GAZP', 'SBER'], tocsv=False)
    print(f)

    # yahoo finance
    bl.yf(['AAPL', 'TSLA'])

    # finam futures
    bl.finam(['Si', 'RTS'], market='futures')

    # biance
    from binance.client import Client
    api_key = 'your api key'
    api_secret = 'your api secret'
    client = Client(api_key, api_secret)
    b = bl.binance(['BTCUSDT', 'BNBETH'], client=client)

    # use saved tickers
    from barloader import tickers as t

    bl.yf(t.usetf)
    bl.finam(t.rufutures, market='futures')
    bl.yf(t.currency, postfix=t.currency.yf_postfix)

    # custom parameters
    start = datetime(2019, 1, 1)
    end = datetime(2019, 2, 1)
    interval = '1h'
    bl.yf(t.usetf, start=start, end=end, interval=interval)
    bl.finam(t.rufutures, market='futures', start=start, end=end, interval=interval)
    bl.yf(t.currency, postfix=t.currency.yf_postfix, start=start, end=end, interval=interval)

    # short notation of custom parameters
    bl.start = datetime(2019, 1, 1)
    bl.end = datetime(2019, 2, 1)
    bl.interval = '1h'

    bl.yf(t.usetf)
    bl.finam(t.rufutures, market='futures')
    bl.yf(t.currency, postfix=t.currency.yf_postfix)
