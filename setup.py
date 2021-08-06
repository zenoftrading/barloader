from setuptools import setup

setup(
   name='Binance downloader',
   version='0.1',
   description='Download history data from binance and save to dataframe or csv file',
   author='Zenoftrading',
   url='https://github.com/zenoftrading/binance_downloader',
   packages=['binance_downloader'],
   install_requires=['pandas', 'tqdm', 'python-binance'],
)