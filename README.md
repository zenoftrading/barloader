# History OHLC data downloader

Download history data from:
- yahoo finance
- finam
- binance

## Requirements

```
python 3+
python-binance
pandas
tqdm
dotmap
finam-export
loguru
yfinance
```

## Install

```
git install git+https://github.com/zenoftrading/barloader.git
```

## Usage

Minimal interface for finam:

```
from barloader.barlodaer import BarLoader

bl = BarLoader()
   
f = bl.finam(['GAZP', 'SBER'], tocsv=False)
print(f)
```

Output:

```
2021-08-20 10:27:43.700 | INFO     | __main__:finam:152 - GAZP
2021-08-20 10:27:51.300 | INFO     | __main__:finam:152 - SBER
[              Open    High     Low   Close    Volume
Date                                                
2021-08-13  292.65  293.90  291.75  292.70  21802270
2021-08-16  291.47  295.48  290.95  295.10  32273890
2021-08-17  295.13  299.50  290.32  298.32  50482060
2021-08-18  299.00  299.95  295.00  295.05  35531240
2021-08-19  293.49  294.72  289.68  293.68  55911470
2021-08-20  293.79  294.90  292.56  293.22   4358120,               Open    High     Low   Close    Volume
Date                                                
2021-08-13  328.60  330.27  327.31  328.68  18758270
2021-08-16  327.56  330.52  327.13  329.36  23916510
2021-08-17  329.00  335.70  328.55  334.50  42463620
2021-08-18  336.05  338.99  333.26  334.90  36270350
2021-08-19  333.50  334.00  329.10  332.69  45936410
2021-08-20  332.20  333.27  330.33  330.47   3527750]
```

Minimal interface for yahoo finance:

```
from barloader.barlodaer import BarLoader

bl = BarLoader()

bl.yf(['AAPL', 'TSLA'])
```

Minimal interface for finam futures:

```
from barloader.barlodaer import BarLoader

bl = BarLoader()

bl.finam(['Si', 'RTS'], market='futures')
```

Minimal interface for binance:

```
from barloader.barloader import BarLoader
from binance.client import Client

bl = BarLoader()
api_key = 'your binance api key'
api_secret = 'your binance api secret'
client = Client(api_key, api_secret)

bl.binance(['BTCUSDT', 'BNBETH'], client=client)
```

All data will be downloaded to folder '1d'.

For fast access to tickers library get saved some tickers in file `tickers.py`

```
from barloader import tickers as t

bl.yf(t.usetf)
bl.finam(t.rufutures, market='futures')
bl.yf(t.currency, postfix=t.currency.yf_postfix)
```

Set custom start end data and interval:

```
from datetime import datetime

start = datetime(2019, 1, 1)
end = datetime(2019, 2, 1)
interval = '1h'
bl.yf(t.usetf, start=start, end=end, interval=interval)
bl.finam(t.rufutures, market='futures', start=start, end=end, interval=interval)
bl.yf(t.currency, postfix=t.currency.yf_postfix, start=start, end=end, interval=interval)
```

Or use short notation:

```
from datetime import datetime

bl = BarLoader()
bl.start = datetime(2019, 1, 1)
bl.end = datetime(2019, 2, 1)
bl.interval = '1h'

bl.yf(t.usetf)
bl.finam(t.rufutures, market='futures')
bl.yf(t.currency, postfix=t.currency.yf_postfix)
```
