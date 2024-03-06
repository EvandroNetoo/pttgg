from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, time
from django.utils import timezone
import json
import requests
from core.settings import RIOT_TOKEN
from typing import Dict, List, Tuple
from summoners.models import (
    Match,
    Summoner,
    RankedSoloDuo,
    RankedFlex,
    SummonerMatch,
)
from django.db.models import QuerySet


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

    def update_summoner_info(
        self, region: str, puuuid: str, game_name: str, tag_line: str
    ) -> dict:
        summoner_data = self.get_summoner_by_puuid(puuuid, region)

        summoner = Summoner.objects.filter(id=summoner_data.get('id'))

        if summoner.exists():
            summoner = summoner.first()
        else:
            summoner = Summoner(
                id=summoner_data.get('id'),
                puuid=summoner_data.get('puuid'),
                name=summoner_data.get('name'),  # Old game name system
            )

        summoner.game_name = game_name
        summoner.tag_line = tag_line
        summoner.profile_icon_id = summoner_data.get('profileIconId')
        summoner.level = summoner_data.get('summonerLevel')

        summoner.save()
        #
        #
        #
        ranked_solo_duo, ranked_flex = self.get_rankeds_infos_by_summoner_id(
            summoner.id, region
        )

        ranked_solo_duo_model = RankedSoloDuo.objects.filter(summoner=summoner)
        if ranked_solo_duo:
            if ranked_solo_duo_model.exists():
                ranked_solo_duo_model = ranked_solo_duo_model.first()
            else:
                ranked_solo_duo_model = RankedSoloDuo(summoner=summoner)

            ranked_solo_duo_model.tier = ranked_solo_duo.get('tier')
            ranked_solo_duo_model.rank = ranked_solo_duo.get('rank')
            ranked_solo_duo_model.pdls = ranked_solo_duo.get('leaguePoints')
            ranked_solo_duo_model.wins = ranked_solo_duo.get('wins')
            ranked_solo_duo_model.losses = ranked_solo_duo.get('losses')

        elif not ranked_solo_duo and ranked_solo_duo_model.exists():
            ranked_solo_duo_model = ranked_solo_duo_model.first()
            ranked_solo_duo_model.delete()
            ranked_solo_duo_model = RankedSoloDuo(summoner=summoner)

        else:
            ranked_solo_duo_model = RankedSoloDuo(summoner=summoner)

        ranked_solo_duo_model.save()
        #
        #
        #
        ranked_flex_model = RankedFlex.objects.filter(summoner=summoner)
        if ranked_flex:
            if ranked_flex_model.exists():
                ranked_flex_model = ranked_flex_model.first()
            else:
                ranked_flex_model = RankedFlex(summoner=summoner)

            ranked_flex_model.tier = ranked_flex.get('tier')
            ranked_flex_model.rank = ranked_flex.get('rank')
            ranked_flex_model.pdls = ranked_flex.get('leaguePoints')
            ranked_flex_model.wins = ranked_flex.get('wins')
            ranked_flex_model.losses = ranked_flex.get('losses')

        elif not ranked_flex and ranked_flex_model.exists():
            ranked_flex_model = ranked_flex_model.first()
            ranked_flex_model.delete()
            ranked_flex_model = RankedFlex(summoner=summoner)

        else:
            ranked_flex_model = RankedFlex(summoner=summoner)

        ranked_flex_model.save()

        return {
            'summoner': summoner,
            'ranked_solo_duo': ranked_solo_duo_model,
            'ranked_flex': ranked_flex_model,
        }

    def get_matches_by_puuid(
        self, puuid: str, start: int = 0, count: int = 5
    ) -> list:
        base_url = self.riot_regional_api_endpoints['AMERICAS']
        endpoint = f'/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}'
        url = base_url + endpoint
        response = self._get(url)

        return response.json()

    def get_match_details(self, match_id: str) -> dict:
        base_url = self.riot_regional_api_endpoints['AMERICAS']
        endpoint = f'/lol/match/v5/matches/{match_id}'
        url = base_url + endpoint
        response = self._get(url)

        return response.json()

    def get_matches_details(self, match_ids: List[str]) -> List[dict]:
        with ThreadPoolExecutor(max_workers=5) as executor:
            matches_details = executor.map(self.get_match_details, match_ids)

        return [match_details for match_details in matches_details]

    def update_matches_details(self, puuid: str) -> None:
        matches = self.get_matches_by_puuid(puuid)
        matches_details = self.get_matches_details(matches)

        with open('queues.json', 'r') as queues:
            queues = json.load(queues)

        for match_detail in matches_details:
            match = Match.objects.filter(
                id=match_detail['metadata']['matchId']
            )
            if not match.first():
                h_duration = int(
                    match_detail['info']['gameDuration'] / 60 / 60
                )
                m_duration = int(
                    match_detail['info']['gameDuration'] / 60 - h_duration * 60
                )
                s_duration = (
                    match_detail['info']['gameDuration']
                    - m_duration * 60
                    - h_duration * 60 * 60
                )
                end_at_naive_datetime = datetime.fromtimestamp(
                    int(match_detail['info']['gameEndTimestamp'] / 1000)
                )
                end_at_aware_datetime = timezone.make_aware(
                    end_at_naive_datetime, timezone.get_current_timezone()
                )
                match = Match(
                    id=match_detail['metadata']['matchId'],
                    end_at=end_at_aware_datetime,
                    duration=time(
                        hour=h_duration,
                        minute=m_duration,
                        second=s_duration,
                    ),
                    queue_id=match_detail['info']['queueId'],
                    queue_type=list(
                        filter(
                            lambda queue: queue['queueId']
                            == match_detail['info']['queueId'],
                            queues,
                        )
                    )[0]['description'],
                )

                match.save()

                match_detail = match_detail['info']

                for summoner in match_detail['participants']:
                    summoner_model = Summoner.objects.filter(
                        id=summoner['summonerId'],
                    )

                    if summoner_model.exists():
                        summoner_model = summoner_model.first()
                    else:
                        summoner_model = Summoner(
                            id=summoner['summonerId'],
                            puuid=summoner['puuid'],
                            name=summoner['summonerName'],
                            game_name=summoner['riotIdGameName'],
                            tag_line=summoner['riotIdTagline'],
                        )
                        summoner_model.save()
                        RankedSoloDuo.objects.create(summoner=summoner_model)
                        RankedFlex.objects.create(summoner=summoner_model)

                    summoner_match = SummonerMatch(
                        summoner=summoner_model,
                        match=match,
                        kills=summoner['kills'],
                        deaths=summoner['deaths'],
                        assists=summoner['assists'],
                        gold_earned=summoner['goldEarned'],
                        itens={
                            'item0': summoner['item0'],
                            'item1': summoner['item1'],
                            'item2': summoner['item2'],
                            'item3': summoner['item3'],
                            'item4': summoner['item4'],
                            'item5': summoner['item5'],
                            'item6': summoner['item6'],
                        },
                        wards_placed=summoner['wardsPlaced'],
                        wards_killed=summoner['wardsKilled'],
                        vision_wards_bought=summoner[
                            'visionWardsBoughtInGame'
                        ],
                        total_damage_dealt=summoner[
                            'totalDamageDealtToChampions'
                        ],
                        total_damage_taken=summoner['totalDamageTaken'],
                        largest_multi_kill=summoner['largestMultiKill'],
                        level=summoner['champLevel'],
                        creep_strike=summoner['neutralMinionsKilled']
                        + summoner['totalMinionsKilled'],
                        summoner1_id=summoner['summoner1Id'],
                        summoner2_id=summoner['summoner2Id'],
                        team='B' if summoner['teamId'] == 100 else 'R',
                        position=summoner['teamPosition'],
                        win=summoner['win'],
                    )

                    summoner_match.save()

    def get_formated_matches_data(self, summoner: Summoner) -> List:
        summoner_matches = SummonerMatch.objects.filter(
            summoner=summoner
        ).all()
        summoner_matches.order_by('-match__end_at')
        summoner_matches = summoner_matches[0:10]
        print(summoner_matches)

        matches_data = []
        for summoner_match in summoner_matches:
            match = summoner_match.match

            all_partcipants = SummonerMatch.objects.filter(match=match)

            def organize_team_by_position(team: QuerySet):
                team = [
                    team.get(position='TOP'),
                    team.get(position='JUNGLE'),
                    team.get(position='MIDDLE'),
                    team.get(position='BOTTOM'),
                    team.get(position='TOP'),
                ]

                return team

            blue_side = all_partcipants.filter(team='B')
            red_side = all_partcipants.filter(team='R')

            if match.queue_id in (400, 420, 440):  # aram
                blue_side = organize_team_by_position(blue_side)
                red_side = organize_team_by_position(red_side)

            match.teams = {
                'blue': blue_side,
                'red': red_side,
            }

            matches_data.append(match)

        return matches_data
