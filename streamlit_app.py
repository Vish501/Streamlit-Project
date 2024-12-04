import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf


@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    data = pd.read_html(url)[0]
    data['Headquarters Location'] = data['Headquarters Location'].str.split(';', expand = True)[0]
    data[['HQ City', 'HQ State']] = data['Headquarters Location'].str.split(', ', n = 1, expand = True)
    return data


def main():
    # Renders the page heading and subheading for the web application
    st.markdown('''
    # Stock Bubbles
    **Data Source: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies**
    ''')

    # Setting up User filter options
    st.sidebar.header('Filters')
    stock_data = load_data()
    sectors = stock_data['GICS Sector'].unique()
    sub_sectors = stock_data['GICS Sub-Industry'].unique()
    city = stock_data['HQ City'].unique()
    state = stock_data['HQ State'].unique()


    stock_data

if __name__ == '__main__':
    main()
