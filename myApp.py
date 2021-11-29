import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
# Simple Stock Price App

These are the stock closing price and volume of Google!

""")

#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDF = tickerData.history(period='id', start='2010-11-28', end='2021-11-28')

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDF.Volume)
