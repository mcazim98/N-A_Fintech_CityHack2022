import pandas as pd 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.request import Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")
print('hello')
n = 10 #the # of article headlines displayed per ticker
# tickers = ['AAPL']
def get_Stock_news(tickers):
    # news_tables = []
    finwiz_url = 'https://finviz.com/quote.ashx?t='
    news_tables = {}
    for ticker in tickers:
        url = finwiz_url + ticker
        # print(url)
        req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
        resp = urlopen(req)    
        html = BeautifulSoup(resp, features="lxml")
        news_table = html.find(id='news-table')
        news_tables[ticker] = news_table
        
    # print(news_tables)
    urls = [] 
    try:
        for ticker in tickers:
            df = news_tables[ticker]
            df_tr = df.findAll('tr')
            df_links = df.findAll('href')
        
            # print ('\n')
            # print ('Recent News Headlines for {}: '.format(ticker))
            
            for i, table_row in enumerate(df_tr):
                a_text = table_row.a.text
                td_text = table_row.td.text
                td_text = td_text.strip()
                # print(a_text,'(',td_text,')')
                if i == n-1:
                    break
            for a in df.find_all('a', href=True):
                print("Found the URL:", a['href'])
                urls.append(a['href'])
    except KeyError:
        pass

    parsed_news = []
    for file_name, news_table in news_tables.items():
        for x in news_table.findAll('tr'):
            text = x.a.get_text() 
            date_scrape = x.td.text.split()

            if len(date_scrape) == 1:
                time = date_scrape[0]
                
            else:
                date = date_scrape[0]
                time = date_scrape[1]

            ticker = file_name.split('_')[0]
            
            parsed_news.append([text, ticker, date, time])
    # print(parsed_news)

    analyzer = SentimentIntensityAnalyzer()

    columns = ['Headline', 'Ticker', 'Date', 'Time']
    news = pd.DataFrame(parsed_news, columns=columns)
    scores = news['Headline'].apply(analyzer.polarity_scores).tolist()

    df_scores = pd.DataFrame(scores)
    news = news.join(df_scores['compound'], rsuffix='_right')
    news["url"] = urls
    print(news.columns)
    print(news)
    return news

