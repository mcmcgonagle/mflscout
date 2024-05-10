import streamlit as st

st.set_page_config(
    page_title="MFL Opponent Scout",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from utility_functions.clubs import find_clubs, get_squad_matches
from utility_functions.matches import get_match
from utility_functions.stat_calculations import record_by_formation
import pandas as pd


club_name = st.text_input("Type a club name to search",'')
try:
    club = st.selectbox("Select a club to scout",find_clubs(club_name))
    number_of_matches = st.slider("How many matches do you want to scout?", 10, 100, 25)
    st.divider()
    club_matches = get_squad_matches(club[1],number_of_matches)

    match_results = []


    for item in club_matches:
        result = get_match(item)
        match_results.append(result)

    scouted_team = record_by_formation(club[1],match_results)

    df = pd.DataFrame.from_dict(scouted_team,orient='index')

    st.dataframe(df,column_config={
            "": "Formation",
            "wins": st.column_config.NumberColumn(
                "Wins"
            ),
            "draws": st.column_config.NumberColumn(
                "Draws"
            ),
            "losses": st.column_config.NumberColumn(
                "Losses"
            )
            },
            use_container_width=True)
    st.divider() 


    st.bar_chart(df,height=450)

except:
    print('user must type to search')
