import requests
import time
import streamlit as st

@st.cache_data(ttl=1800)
def get_match(id):
    try:
        #print(id)
        url = 'https://z519wdyajg.execute-api.us-east-1.amazonaws.com/prod/matches/' + str(id) + '?withFormations=true'
        #print(url)
        r = requests.get(url)
        match = {
            'home': {
                'formation': r.json()['homeFormation']['type'],
                'score': r.json()['homeScore'],
                'id': r.json()['homeSquad']['club']['id'],
                'name': r.json()['homeTeamName']
            },
            'away': {
                'formation': r.json()['awayFormation']['type'],
                'score': r.json()['awayScore'],
                'id': r.json()['awaySquad']['club']['id'],
                'name': r.json()['awayTeamName']
            }
        }
        #print(match)
        return match
    except:
        print('error for match')
        

