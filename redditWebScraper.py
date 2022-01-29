import praw
import requests
import pandas as pd

reddit = praw.Reddit(
    client_id="qlosPf8oOYUqmeI88mQ0GA",
    client_secret="tPFqBh6gngtuKTeKTnXw5Y7sDC0jTw",
    password="305503#alvi",
    user_agent="senti_scraper",
    username="liav305",
)

subreddits_stock = ['wallstreetbets','stocks','InvestingandTrading','pennystocks','robinhood']
subreddits_crypto = ['bitcoin','CryptoCurrency','bitcoinbeginners','CryptoMarkets','icocrypto']

stock = input("Input stock name")

coin = input("Input coin name")

#for making dataframe of stocks

stock_posts = []


for sub in subreddits_stock:
    print(sub.upper())
    subrdts = reddit.subreddit(sub).search(stock)
    for post in list(subrdts)[0:10]:
        print(post.title)
        sentimentScore = 0.98
        engagementRate = 0.66
        stock_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments,sentimentScore,engagementRate])
        
stock_posts = pd.DataFrame(stock_posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments','sentimentScore','engagementRate'])
stock_posts.to_csv('stock_data.csv') 


    
# for making dataframe 

crypto_posts = []

for subs in subreddits_crypto:
    print(subs.upper())
    subrdt = reddit.subreddit(sub).search(coin)
    for post_1 in list(subrdt)[0:10]:
        print(post_1.title)
        sentimentScore = 0.98
        engagementRate = 0.66
        crypto_posts.append([post_1.title, post_1.score, post_1.id, post_1.subreddit, post_1.url, post_1.num_comments,sentimentScore,engagementRate])
        
crypto_posts = pd.DataFrame(crypto_posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments','sentimentScore','engagementRate'])
crypto_posts.to_csv('crypto_data.csv') 