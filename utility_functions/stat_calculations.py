games = [{'home': {'formation': '3-5-2', 'score': 3, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-3-1-2', 'score': 1, 'id': 494, 'name': 'MUC Sampdoria'}}, {'home': {'formation': '4-2-3-1', 'score': 0, 'id': 186, 'name': 'Sporting Tunis'}, 'away': {'formation': '3-5-2', 'score': 4, 'id': 136, 'name': 'Valencia Legionarios MFC'}}, {'home': {'formation': '4-1-2-1-2', 'score': 0, 'id': 659, 'name': 'Great Pyramids MFC'}, 'away': {'formation': '3-5-2', 'score': 7, 'id': 136, 'name': 'Valencia Legionarios MFC'}}, {'home': {'formation': '4-4-2', 'score': 4, 'id': 678, 'name': 'VALOR FC'}, 'away': {'formation': '3-5-2', 'score': 1, 'id': 136, 'name': 'Valencia Legionarios MFC'}}, {'home': {'formation': '3-5-2', 'score': 0, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-1-2-1-2', 'score': 2, 'id': 571, 'name': 'D.C. Cherries'}}, {'home': {'formation': '3-5-2', 'score': 2, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-2-2-2', 'score': 1, 'id': 152, 'name': 'MFC Atlantique'}}, {'home': {'formation': '3-5-2', 'score': 3, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-3-3', 'score': 0, 'id': 498, 'name': 'Pombero MFC'}}, {'home': {'formation': '3-5-2', 'score': 5, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-2-3-1', 'score': 1, 'id': 255, 'name': 'Artificial Asteroids'}}, {'home': {'formation': '4-4-2', 'score': 0, 'id': 292, 'name': 'Craptors'}, 'away': {'formation': '5-3-2', 'score': 0, 'id': 136, 'name': 'Valencia Legionarios MFC'}}, {'home': {'formation': '5-3-2', 'score': 1, 'id': 136, 'name': 'Valencia Legionarios MFC'}, 'away': {'formation': '4-3-3', 'score': 1, 'id': 99, 'name': 'Galway Grizzlys'}}]
id = 136

def home_or_away(id,game):
    if game['home']['id'] == id:
        return 'home'
    else:
        return 'away'


def record_by_formation(id,games):
    formations = {}
    for item in games:
        scout_team = home_or_away(id,item)
        if scout_team == 'home':
            other_team = 'away'
        else:
            other_team = 'home'
        if item[scout_team]['score'] > item[other_team]['score']:
            formations
            formations[item[scout_team]['formation']['wins']] += 1
        elif item[scout_team]['score'] == item[other_team]['score']:
            formations[item[scout_team]['formation']['draws']] += 1
        else:
            formations[item[scout_team]['formation']['losses']] += 1
    print(formations)
        

def avg_score_by_formation(id,games):
    pass

def goal_differential_by_formation(id,games):
    pass

record_by_formation(id,games)