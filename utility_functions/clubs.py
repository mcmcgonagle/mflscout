import requests


def get_club_squad(id):
    url = 'https://z519wdyajg.execute-api.us-east-1.amazonaws.com/prod/clubs/'+str(id)
    r = requests.get(url)
    squad = r.json()['squads'][0]['id']
    return squad

def get_squad_matches(id):
    squad = get_club_squad(id)
    matches = []
    url = 'https://z519wdyajg.execute-api.us-east-1.amazonaws.com/prod/matches?squadId='+str(squad)+'&past=true&limit=10'
    r = requests.get(url)
    for item in r.json():
        matches.append(item['id'])
    return matches


def find_clubs(club_name):
    url = 'https://z519wdyajg.execute-api.us-east-1.amazonaws.com/prod/leaderboards/clubs/global?clubName=' + club_name +'&sort=nbMflPoints&sortOrder=DESC&limit=20'
    r = requests.get(url)
    found_clubs = []
    for item in r.json()['clubs']:
        found_clubs.append([item['name'],item['id'] ])
    return found_clubs

