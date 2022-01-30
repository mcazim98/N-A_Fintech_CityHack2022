import praw
import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")
reddit = praw.Reddit(
    client_id="qlosPf8oOYUqmeI88mQ0GA",
    client_secret="tPFqBh6gngtuKTeKTnXw5Y7sDC0jTw",
    password="305503#alvi",
    user_agent="senti_scraper",
    username="liav305",
)

def scraper_stock(stock):


        subreddits_stock = ['wallstreetbets','stocks']
        # 'InvestingandTrading','pennystocks','robinhood']
        

       

        #for making dataframe of stocks

        stock_posts = []


        for sub in subreddits_stock:
            print(sub.upper())
            subrdts = reddit.subreddit(sub).search(stock)
            for post in list(subrdts)[0:10]:
                print(post.title)
                # sentimentScore = 0.98
                # engagementRate = 0.66
                stock_posts.append([post.title, post.score, post.id, sub, post.url, post.num_comments])
         
        stock_posts = pd.DataFrame(stock_posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments'])
        analyzer = SentimentIntensityAnalyzer()
        scores = stock_posts['title'].apply(analyzer.polarity_scores).tolist()
        df_scores = pd.DataFrame(scores)
        news = stock_posts.join(df_scores['compound'], rsuffix='_right')
        return news


    

def scraper_crypto(coin):
    
        crypto_posts = []
        subreddits_crypto = ['bitcoin','CryptoCurrency']
        # ,'bitcoinbeginners','CryptoMarkets','icocrypto']

        for sub in subreddits_crypto:
            print(sub.upper())
            subrdt = reddit.subreddit(sub).search(coin)
            for post_1 in list(subrdt)[0:10]:
                print(post_1.title)
                crypto_posts.append([post_1.title, post_1.score, post_1.id, sub, post_1.url, post_1.num_comments])
                
        crypto_posts = pd.DataFrame(crypto_posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments'])
        analyzer = SentimentIntensityAnalyzer()
        scores = crypto_posts['title'].apply(analyzer.polarity_scores).tolist()
        df_scores = pd.DataFrame(scores)
        news = crypto_posts.join(df_scores['compound'], rsuffix='_right')
        # print(news)
        return news

# scraper_crypto("bitcoin")