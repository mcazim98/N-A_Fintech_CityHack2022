from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
def getCurrPrice(coinName):
    currentPrice = cg.get_price(ids=coinName, vs_currencies='usd')
    vals = [[coinName,currentPrice[coinName]['usd']]]
    df = pd.DataFrame(vals, columns=['name', "price"])
    return df
def getChart(coinName):
    chart = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='30')
    prices = []
    for a in chart['prices']:
        prices.append(a[1])
    df = pd.DataFrame(prices, columns=['price'])
    return df
