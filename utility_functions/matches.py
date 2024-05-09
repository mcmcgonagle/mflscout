import requests
import time

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
        time.sleep(0.5)
        return match
    except:
        print('error for match')

