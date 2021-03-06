from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
def getCurrPrice(coinName):
    currentPrice = cg.get_price(ids=coinName, vs_currencies='usd')
    print(currentPrice)
    vals = [[coinName,currentPrice[coinName.lower()]['usd']]]
    df = pd.DataFrame(vals, columns=['name', "price"])
    return df
def getChart(coinName):
    chart = cg.get_coin_market_chart_by_id(id=coinName.lower(),vs_currency='usd',days='30')
    prices = []
    for a in chart['prices']:
        # print(a)
        prices.append([a[0], a[1]])
    df = pd.DataFrame(prices, columns=['Date','price'])
    # print(ans)
    return df

# print(getChart("Cardano"))