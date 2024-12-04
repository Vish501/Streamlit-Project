from datetime import datetime
import pandas as pd
import streamlit as st

@st.cache_data
def data_loader(year: int):
    # Loading the data from the website and caching it to prevent multiple queries
    # Also dropping the Rk column, since Pandas is already maintinaing it
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'
    data = pd.read_html(url)[0]
    data = data.drop(['Rk'], axis = 1)
    data = data[data['Team'].notna()]
    data.index += 1
    return data


def csv_download(data):
    return data.to_csv().encode('utf-8')


def main():
    # Renders the page heading and subheading for the web application
    st.write('''
    # NBA Player Stats Explorer
    ###### Data Source: https://www.basketball-reference.com/
    ''')


    # Input Selection Menu (Year, Team, Position)
    # Also loading the data using year to help build Team and Position lists
    st.sidebar.header('Filters')
    year = st.sidebar.selectbox('Year', list(range(1947, datetime.now().year))[::-1])

    player_stats = data_loader(year)
    available_teams = player_stats.Team.unique()
    available_positions = player_stats.Pos.unique()
    
    teams = st.sidebar.multiselect('Team', available_teams, available_teams)
    positions = st.sidebar.multiselect('Position', available_positions, available_positions)
    

    # Filtering the data and rendering it
    player_stats_selected = player_stats[player_stats.Team.isin(teams) & player_stats.Pos.isin(positions)]
    st.header('Stats of the Filtered Team')
    st.write(f'Size: **{player_stats_selected.shape[0]} players** and their **{player_stats_selected.shape[1]} data points.**')
    st.dataframe(player_stats_selected)


    # Allowing for the filtered data to be downloaded
    st.download_button('Press to Download the Filtered Data', csv_download(player_stats_selected), 'basketball_player_data.csv', 'text/csv', key = 'download-csv')


if __name__ == '__main__':
    main()
