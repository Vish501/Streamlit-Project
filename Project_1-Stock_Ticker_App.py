import pandas as pd
import streamlit as st
import yfinance as yf

def check_available(ticker: str) -> bool:
    # Checks if a Ticker is available via the Yahoo Finance API
    info = yf.Ticker(ticker).history(period='1d', interval='1d')
    return len(info) > 0


def main():
    st.write("""
    # Stock Price and Volume App
    Check the closing price and volume of the selected NYSE ticker!
    """)

    ticker = st.text_input("Enter NYSE Ticker", "GOOGL")

    if check_available(ticker) == False:
        st.markdown('Invalid Ticker')
    else:
        ticker_data = yf.Ticker(ticker)
        ticker_dataframe = ticker_data.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

        st.line_chart(ticker_dataframe.Close, y_label = 'Price in USD $')
        st.line_chart(ticker_dataframe.Volume, y_label = 'Volume')


if __name__ == '__main__':
    main()
