# some tickers need to download
from dotmap import DotMap

imoex = DotMap(
    yf_postfix = '.ME',
    tickers = ['GAZP', 'SBER', 'LKOH', 'GMKN', 'YNDX', 'NVTK', 'ROSN', 'POLY', 'TCSG', 'PLZL', \
        'MGNT', 'TATN', 'NLMK', 'CHMF', 'SNGS', 'MTSS', 'ALRS', 'SNGS', 'FIVE', 'MOEX', 'MAIL', \
        'IRAO', 'VTBR', 'OZON', 'PHOR', 'RUAL', 'PIKK', 'MAGN', 'AFKS', 'RTKM', 'DSKY', 'TRNFP', \
        'HHRU', 'AFLT', 'HYDR', 'POGR', 'TATN', 'FEES', 'GLTR', 'CBOM', 'LSRG', 'RSTI', 'QIWI'], # .ME yfinance
)

moex10 = DotMap(
    yf_postfix = '.ME',
    tickers = ['MAGN', 'GMKN', 'POLY', 'GAZP', 'SBER', 'YNDX', 'LKOH', 'ROSN', 'AFKS', 'TATN']
)
    
moexbc = DotMap(
    yf_postfix = '.ME',
    tickers = ['FIVE', 'GAZP', 'GMKN', 'LKOH', 'MAIL', 'MGNT', 'MTSS', 'NVTK', 'PLZL', \
        'POLY', 'ROSN', 'SBER', 'SNGS', 'TATN', 'YNDX']
)

# https://www.moex.com/ru/derivatives/select.aspx
# Si, SPFB.Si, sirtsc1, usd/rub 
# RI, SPFB.RTS, rirtsc1, индекс ртс
# BR, SPFB.BR, brrtsc1 нефть brent
# GD, SPFB.GOLD, gdrtsc1, золото
# SR, SPFB.SBRF, srrtsc1 сбербанк
rufutures = DotMap(tickers = ['Si', 'RTS', 'BR', 'GOLD', 'SBRF'])

currency = DotMap(
    yf_postfix = 'USD=X', # RUBUSD=X
    tickers = ['RUB', 'EUR', 'GBP']   
)

crypto = DotMap(
    yf_postfix = '-USD', # BTC-USD
    tickers = ['BTC', 'ETH']
)

usetf = DotMap(
    tickers = ['SPY', 'IVV', 'VTI', 'VOO', 'QQQ', 'VEA', 'IEFA', 'AGG', 'VTV', 'IEMG', 'VWO', 'BND', \
        'VUG', 'IJR', 'IWM', 'IWF', 'IJH', 'GLD', 'VIG', 'EFA', 'IWD', 'VO', 'VXUS', 'VCIT', 'VB', 'XLF', \
        'VGT', 'BNDX', 'LQD', 'VCSH', 'XLK', 'VNQ', 'ITOT', 'VYM', 'VEU', 'BSV', 'IVW', 'EEM', 'DIA', 'IAU', \
        'SCHX', 'IWB', 'IXUS', 'IWR', 'RSP', 'USMV', 'TIP', 'XLV', 'SCHF', 'MBB', 'IGSB', 'SCHD', 'XLE', \
        'VBR', 'VV', 'IVE', 'HYG', 'MUB', 'MDY', 'VT', 'SCHB', 'ARKK', 'XLI', 'QUAL', 'SHY', 'SDY', 'EMB', \
        'XLY', 'DVY', 'PFF', 'DGRO', 'VGK', 'MTUM', 'ESGU', 'SCHP', 'ACWI', 'JPST', 'IWN', 'VLUE', 'GOVT', \
        'VXF', 'GDX', 'SLV', 'SCHA', 'VBK', 'VMBS', 'SHV', 'SCZ', 'VHT', 'IWP', 'BIV', 'VOE', 'MINT', 'SCHG', \
        'IWS', 'EFV', 'VTIP', 'XLC', 'IUSB', 'IEF']
)

sp500 = DotMap(
    tickers = ['MMM', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES', 'AFL', 'A', \
        'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', \
        'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', \
        'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ANET', 'AJG', \
        'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BK', 'BAX', 'BDX', \
        'BRK-B', 'BBY', 'BIO', 'BIIB', 'BLK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', \
        'BF-B', 'CHRW', 'COG', 'CDNS', 'CZR', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', \
        'CBOE', 'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CERN', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', \
        'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', \
        'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST', 'CCI', 'CSX', \
        'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', \
        'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', \
        'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR', 'ENPH', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', \
        'ESS', 'EL', 'ETSY', 'EVRG', 'ES', 'RE', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', \
        'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FRC', 'FISV', 'FLT', 'FMC', 'F', 'FTNT', 'FTV', 'FBHS', 'FOXA', \
        'FOX', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GL', \
        'GPN', 'GS', 'GWW', 'HAL', 'HBI', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', \
        'HFC', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUM', 'HBAN', 'HII', 'IEX', 'IDXX', 'INFO', \
        'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', \
        'IQV', 'IRM', 'JKHY', 'J', 'JBHT', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'KEYS', \
        'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LB', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', \
        'LEN', 'LLY', 'LNC', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', \
        'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MKC', 'MXIM', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', \
        'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MHK', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', \
        'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NSC', \
        'NTRS', 'NOC', 'NLOK', 'NCLH', 'NOV', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', \
        'OMC', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PENN', 'PNR', 'PBCT', \
        'PEP', 'PKI', 'PRGO', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', \
        'PGR', 'PLD', 'PRU', 'PTC', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', \
        'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI',\
        'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SNA', 'SO', 'LUV', 'SWK', \
        'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TGT', \
        'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', \
        'TFC', 'TWTR', 'TYL', 'TSN', 'UDR', 'ULTA', 'USB', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', \
        'UHS', 'UNM', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VIAC', 'VTRS', 'V', 'VNO', 'VMC', \
        'WRB', 'WAB', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WU', 'WRK', 'WY', \
        'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XLNX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']
)