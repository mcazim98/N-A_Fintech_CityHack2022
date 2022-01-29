import streamlit as st
import pandas as pd
import numpy as np
import plotly as plt

# indication options for stock and digital coin

src_stock = "X:\\CityHack2022\\all_data.csv"
stock_df = pd.read_csv(src_stock)
stockList = list(stock_df['col'])


src_coin = "X:\\CityHack2022\\coin.csv"

coin_df = pd.read_csv(src_coin)
coin_df = pd.read_csv(src_coin)

coinList=list(coin_df['col'])


#page_layout

st.set_page_config(layout="wide")



selectbox_stock = st.sidebar.selectbox(
    "Search Stock",
    stockList
)

selectbox_coin = st.sidebar.selectbox(
    "Search Cryto",
    coinList

)


