import streamlit as st
import pandas as pd
import numpy as np
import plotly as plt
import plotly.express as px
from yfinance_data import get_datareader
import plotly.graph_objects as go
import yfinance_data as yfd
import yfinz 
# indication options for stock and digital coin

src_stock = "all_data.csv"
stock_df = pd.read_csv(src_stock)
stockList = list(stock_df['symbol'])


src_coin = "coin.csv"

coin_df = pd.read_csv(src_coin)

coinList=list(coin_df['col'])


#page_layout

st.set_page_config(layout="wide")
col1, col2,col3 = st.sidebar.columns([10,10,10])
col2.header("OneStock")
col2.image("logo.png", width = 150)
stock = st.sidebar.selectbox(
    "Search Stock",
    stockList
)



coin = st.sidebar.selectbox(
    "Search Cryto",
    coinList
)

button = st.sidebar.button("Show")
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
        curr_close, curr_df = yfd.get_current_price(str(stock))
        fig = px.line(curr_df,  x=curr_df.index, y="Close")
        st.header(f"{stock} Chart")
        st.plotly_chart(fig)
        st.subheader(f"The current closing price of {stock} is {float(curr_close)}")
        news = yfinz.get_Stock_news([stock])
        pos_news = news.query("compound > 0").sort_values("compound", ascending = False)
        neg_news = news.query("compound <= 0").sort_values("compound", ascending = True)
        st.subheader(f"Positive News data for {stock} with sentiment values")
        st.dataframe(pos_news)
        st.subheader(f"Negative News data for {stock} with sentiment values")
        st.dataframe(neg_news)

    else:
        headers()

lk()
