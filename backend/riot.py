import requests
from core.settings import RIOT_TOKEN
from typing import Dict, Tuple


class RiotLolApi:
    riot_token = RIOT_TOKEN

    riot_regional_api_endpoints = {
        'AMERICAS': 'americas.api.riotgames.com',
        'ASIA': 'asia.api.riotgames.com',
        'EUROPE': 'europe.api.riotgames.com',
        'SEA': 'sea.api.riotgames.com',
    }

    riot_plataform_api_endpoints = {
        'BR': 'br1.api.riotgames.com',
        'EUN': 'eun1.api.riotgames.com',
        'EUW': 'euw1.api.riotgames.com',
        'JP': 'jp1.api.riotgames.com',
        'KR': 'kr.api.riotgames.com',
        'LAN': 'la1.api.riotgames.com',
        'LAS': 'la2.api.riotgames.com',
        'NA': 'na1.api.riotgames.com',
        'OC': 'oc1.api.riotgames.com',
        'TR': 'tr1.api.riotgames.com',
        'RU': 'ru.api.riotgames.com',
        'PH': 'ph2.api.riotgames.com',
        'SG': 'sg2.api.riotgames.com',
        'TH': 'th2.api.riotgames.com',
        'TW': 'tw2.api.riotgames.com',
        'VN': 'vn2.api.riotgames.com',
    }

    def _get(self, url) -> requests.Response:
        response = requests.get(
            'https://' + url,
            headers={'X-Riot-Token': self.riot_token},
        )
        return response

    def get_puuid_by_riotid(self, game_name: str, tag_line: str) -> str | None:
        base_url = self.riot_regional_api_endpoints['AMERICAS']
        endpoint = (
            f'/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
        )
        url = base_url + endpoint
        response = self._get(url)
        print(self.riot_token)
        return response.json().get('puuid')

    def get_summoner_by_puuid(self, puuid: str, region: str) -> dict:
        base_url = self.riot_plataform_api_endpoints[region.upper()]
        endpoint = f'/lol/summoner/v4/summoners/by-puuid/{puuid}'
        url = base_url + endpoint
        response = self._get(url)

        return response.json()

    def get_rankeds_infos_by_summoner_id(
        self, summoner_id: str, region: str
    ) -> Tuple[Dict | None, Dict | None]:
        base_url = self.riot_plataform_api_endpoints[region.upper()]
        endpoint = f'/lol/league/v4/entries/by-summoner/{summoner_id}'
        url = base_url + endpoint
        response = self._get(url).json()

        ranked_solo_duo = [
            data for data in response if data['queueType'] == 'RANKED_SOLO_5x5'
        ]

        ranked_flex = [
            data for data in response if data['queueType'] == 'RANKED_FLEX_SR'
        ]

        return (
            ranked_solo_duo[0] if ranked_solo_duo else None,
            ranked_flex[0] if ranked_flex else None,
        )
