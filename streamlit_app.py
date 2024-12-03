import pandas as pd
import streamlit as st
import yfinance as yf


def project():
    st.write("""
    # Stock Price App
    Shown are the stock closing price and volume of the selected ticker!
    """)

    ticker = 'GOOGL'
    ticker_data = yf.Ticker(ticker)
    ticker_dataframe = ticker_data.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

    st.line_chart(ticker_dataframe.Close)
    st.line_chart(ticker_dataframe.Volume)


if __name__ == '__main__':
    project()
