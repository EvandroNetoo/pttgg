dados = [
    {
        'leagueId': 'bb1a0a38-cb69-470b-a535-4def1688c4b9',
        'queueType': 'RANKED_SOLO_5x5',
        'tier': 'PLATINUM',
        'rank': 'III',
        'summonerId': 'BQchTmxI5QB14VMlRjckfuEWsgjIpT4sYtJVuOglKxOK6FU',
        'summonerName': 'PETUTI PRIMATA',
        'leaguePoints': 57,
        'wins': 69,
        'losses': 54,
        'veteran': False,
        'inactive': False,
        'freshBlood': True,
        'hotStreak': False,
    },
]

# Filtrar para RANKED_SOLO_5x5
ranked_solo_duo = [
    dado for dado in dados if dado['queueType'] == 'RANKED_SOLO_5x5'
]

# Filtrar para RANKED_FLEX_SR
ranked_flex = [dado for dado in dados if dado['queueType'] == 'RANKED_FLEX_SR']

# Exibir os resultados
print('Ranked Solo/Duo:', ranked_solo_duo)
if ranked_flex:
    print('Ranked Flex:', ranked_flex)
