import streamlit as st
import pandas as pd
import numpy as np
import plotly as plt
import plotly.express as px
from yfinance_data import get_datareader
import plotly.graph_objects as go
import yfinance_data as yfd
import yfinz 
from datetime import datetime
import Data as Dt
import redditScraper as rs
# indication options for stock and digital coin

#Stock
src_stock = "all_data.csv"
stock_df = pd.read_csv(src_stock)
stockSymList = list(stock_df['symbol'])
stockNameList = list(stock_df['companyName'])




src_coin = "coin.csv"

coin_df = pd.read_csv(src_coin)

coinList=list(coin_df['col'])


#page_layout

st.set_page_config(layout="wide")
col1, col2,col3 = st.sidebar.columns([10,25,10])
#col2.title("OneStock")
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>OneStock</h1>", unsafe_allow_html=True)
col2.image("logo.png", width = 150)
stock = st.sidebar.selectbox(
    "Search Stock",
    stockNameList
    )
button = st.sidebar.button("Show Stock")
# finding symbol corresponding with name for stock

ind_pos = stockNameList.index(stock)

stockSymbol = stockSymList[ind_pos]




coin = st.sidebar.selectbox(
    "Search Crypto",
    coinList
)

button2 = st.sidebar.button("Show Coin")
def headers():
    st.header("WELCOME TO OneStock")
    st.subheader("""We are the one stop gateway""")

    df1, df2 = get_datareader()

    fig = px.line(df2,  x=df2.index, y="Close")
    fig2 = px.line(df1, x=df1.index, y="Close")
    st.subheader("HANG SENG INDEX")
    st.plotly_chart(fig)
    st.subheader("NASDAQ")
    st.plotly_chart(fig2)

def lk():
    if button:
        st.empty()
        curr_close, curr_df = yfd.get_current_price(str(stockSymbol))
        fig = px.line(curr_df,  x=curr_df.index, y="Close")
        st.header(f"{stock} Chart")
        st.plotly_chart(fig)
        st.subheader(f"The current closing price of {stock} is {float(curr_close)}")
        news = yfinz.get_Stock_news([stockSymbol])
        pos_news = news.query("compound > 0").sort_values("compound", ascending = False)
        neg_news = news.query("compound <= 0").sort_values("compound", ascending = True)
        st.subheader(f"Positive News data for {stock} with sentiment values")
        st.dataframe(pos_news)
        st.subheader(f"Negative News data for {stock} with sentiment values")
        st.dataframe(neg_news)

        news = rs.scraper_stock(stock)
        pos_news = news.query("compound > 0").sort_values("compound", ascending = False)
        neg_news = news.query("compound <= 0").sort_values("compound", ascending = True)
        st.subheader(f"Positive Reddit News data for {stock} with sentiment values")
        st.dataframe(pos_news)
        st.subheader(f"Negative Reddit News data for {stock} with sentiment values")
        st.dataframe(neg_news)

    elif button2:
        st.empty()
        curr_price_df = Dt.getCurrPrice(coin)
        curr_price = curr_price_df['price']

        st.subheader(f"The current closing price of {coin} is {float(curr_price)}")
        st.header(f"{coin} Chart")
        hist_price_df =Dt.getChart(coin)
        listdummy = []
        curr_close, curr_df = yfd.get_current_price(str(stockSymbol))
        listdummy = curr_df.index[0:len(hist_price_df)]
    
        hist_price_df["time"] = listdummy

        fig1 = px.line(hist_price_df, x = "time", y ="price" )
        st.plotly_chart(fig1)

        # st.write(hist_price_df)
        # fig1 = px.line(hist_price_df, x = timestamp, y ="price" )
        # st.plotly_chart(fig1)

        #sentiment analysis
        news = rs.scraper_crypto(coin)
        pos_news = news.query("compound > 0").sort_values("compound", ascending = False)
        neg_news = news.query("compound <= 0").sort_values("compound", ascending = True)
        st.subheader(f"Positive News data for {coin} with sentiment values")
        st.dataframe(pos_news)
        st.subheader(f"Negative News data for {coin} with sentiment values")
        st.dataframe(neg_news)
        # print(df_crypto_snt)
        # st.write(df_crypto_snt)
    else:
        headers()

lk()