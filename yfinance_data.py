import yfinance as yf

def get_current_price(tickerSymbol):
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2012-1-1', end='2022-1-29')
    return tickerDf.tail(1), tickerDf.tail(200)



curr_price, historical_data = get_current_price("AAPL")
print(curr_price)