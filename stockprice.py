import yfinance as yf
import pandas as pd
import streamlit as st
import datetime as dt

st.write("""
         ## Stock Price App
         Find below the stock **closing price** and the ** volume **
         of the selected company
          """)

stocklist = {'Google':'GOOGL' ,'Amazon':'AMZN','Facebook':'FB',
             'Microsoft':'MSFT','Apple':'AAPL'}
 
start_date = dt.date(2010, 1,1)
end_date = dt.date(2021,10,1)

selection = st.selectbox('Pick the stock name from the dropdown',
                         stocklist.keys())

daterange = st.slider("Select date range", value=[start_date,end_date])
date_input = st.date_input('Pick date from calendar',value=[daterange[0],daterange[1]], min_value=start_date,
              max_value=end_date)
 
tickersymbol = selection
tickerdata = yf.Ticker(stocklist.get(selection))

tickerdf = tickerdata.history(period='1d', start=str(daterange[0]),
                              end=str(daterange[1]))

st.write("""
         ### Closing price
         """)
st.line_chart(tickerdf.Close)

st.write("""
         ### Volume
         """)
st.line_chart(tickerdf.Volume)

 
