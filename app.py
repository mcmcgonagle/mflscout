import streamlit as st
from utility_functions.clubs import find_clubs, get_squad_matches
from utility_functions.matches import get_match


club_name = st.text_input("Type a club name to search",'Valencia')
club = st.selectbox("Select a club to scout",find_clubs(club_name))


club_matches = get_squad_matches(club[1])


match_results = []

for item in club_matches:
    result = get_match(item)
    match_results.append(result)

for item in match_results:
    print(item)
