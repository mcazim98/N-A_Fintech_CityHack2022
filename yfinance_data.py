# import yfinance as yf
import pandas_datareader as pdr
import pandas as pd
def get_current_price(tickerSymbol):
    ts = pdr.av.time_series.AVTimeSeriesReader(tickerSymbol, api_key="FUUBRJEHY61W5JXW")
    df = ts.read()
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    return df
    
def get_nas_and_hsi():
    tickerData = yf.Ticker("^HSI")
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2012-1-1', end='2022-1-29')
    tickerData2 = yf.Ticker("^NASDAQ")
    tickerDF2  = tickerData2.history(period='1h', start='2012-1-1', end='2022-1-29')
    return tickerDf.tail(200), tickerDf2.tail(200)

def get_datareader(stock_symbol, stock_symbol2):
    ts = pdr.av.time_series.AVTimeSeriesReader(stock_symbol, api_key="FUUBRJEHY61W5JXW")
    df = ts.read()
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    # plotting the opening and closing value 
    # df[['open','close']].plot()
    # print(float(df.tail(1)['close']))
    ts2 = pdr.av.time_series.AVTimeSeriesReader(stock_symbol2, api_key="FUUBRJEHY61W5JXW")
    df2 = ts2.read()
    df2.index = pd.to_datetime(df2.index, format='%Y-%m-%d')
    return df.tail(100), df2.tail(100) 
# curr_price, historical_data = get_nas_and_hsi()
# print(curr_price)
# get_datareader("TSLA", "AAPL")