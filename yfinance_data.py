import yfinance as yf
import pandas_datareader as pdr
import pandas as pd
def get_current_price(tickerSymbol):
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2012-1-1', end='2022-1-29')
    return tickerDf.tail(1)["Close"],tickerDf 

def get_nas_and_hsi(ticker_name):
    tickerData = yf.Ticker(ticker_name.upper())
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2012-1-1', end='2022-1-29')
    return tickerDf

def get_datareader():
    tickerData1 = yf.Ticker("^IXIC")
    #get the historical prices for this ticker
    tickerDf1 = tickerData1.history(period='1h', start='2012-1-1', end='2022-1-29')
    # plotting the opening and closing value 
    # df[['open','close']].plot()
    # print(float(df.tail(1)['close']))
    tickerData = yf.Ticker("^HSI")
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2012-1-1', end='2022-1-29')
    return tickerDf1.tail(100), tickerDf.tail(100)
# curr_price, historical_data = get_nas_and_hsi()
# print(curr_price)

# print(get_current_price("AAPL"))