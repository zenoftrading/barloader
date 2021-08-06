# Binance history data downloader

Download history data from binance and save to dataframe or csv file

## Requirements

```
python 3+
python-binance
pandas
tqdm
```

## Install

```
git install git+https://github.com/zenoftrading/binance_downloader.git
```

## Usage

Minimal interface:

```
from binance.client import Client
from binance_downloader import binance_downloader as bd

api_key = 'your binance api key'
api_secret = 'your binance api secret'

client = Client(api_key, api_secret)

candles = bd.get(client)
print(candles)
```

Output:

```
downloading BTCUSDT 1h from 2021-08-05 14:55:59 to 2021-08-06 14:55:59
                               open            high             low           close         volume
dateTime                                                                                          
2021-08-05 15:00:00  39005.30000000  39370.00000000  38545.59000000  38750.01000000  5612.00309000
2021-08-05 16:00:00  38750.00000000  39779.00000000  38737.31000000  39739.72000000  5641.43756100
...
2021-08-06 13:00:00  40762.87000000  41025.00000000  40700.68000000  40924.07000000  2340.43658100
2021-08-06 14:00:00  40924.08000000  40973.42000000  40649.89000000  40768.81000000  1563.73017300
```

Get custom data:

```
from binance.client import Client
from binance_downloader import binance_downloader as bd
from datetime import datetime

api_key = 'your binance api key'
api_secret = 'your binance api secret'

client = Client(api_key, api_secret)

coin = 'ETHUSDT'
interval = '1m' # support '1m', '1h' or '1d'
start = datetime(2018, 1, 1)
end = datetime(2018, 1, 2)
candles = bd.get(client, coin=coin, interval=interval, start=start, end=end, to_csv=True)
print(candles)
```

Output:

```
downloading ETHUSDT 1m from 2018-01-01 00:00:00 to 2018-01-02 00:00:00
1441it [00:01, 780.52its]           
saved to ETHUSDT_1m.csv
                             open          high           low         close        volume
dateTime                                                                                 
2018-01-01 00:00:00  733.01000000  733.97000000  732.75000000  732.75000000   19.77247000
2018-01-01 00:01:00  733.34000000  734.52000000  732.51000000  732.51000000   26.05199000
...                           ...           ...           ...           ...           ...
2018-01-01 23:59:00  755.00000000  755.01000000  754.34000000  754.99000000   40.92658000
2018-01-02 00:00:00  754.99000000  757.76000000  754.34000000  757.76000000  108.80959000

[1441 rows x 5 columns]
```