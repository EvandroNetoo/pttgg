from datetime import datetime, time
import json
from typing import List
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Router
from summoners.models import (
    Summoner,
    RankedSoloDuo,
    RankedFlex,
    Match,
    SummonerMatch,
)
from .schemas import MatchOut, SummonerInfosOut
from riot import RiotLolApi
from django.utils import timezone
from django.db.models import QuerySet


summoners_router = Router()


@summoners_router.get(
    '{region}/{game_name}-{tag_line}',
    response={200: SummonerInfosOut, 404: dict},
)
def get_summoners_infos(
    request: HttpRequest, region: str, game_name: str, tag_line: str
) -> HttpResponse:
    riot = RiotLolApi()

    puuuid = riot.get_puuid_by_riotid(game_name, tag_line)

    if puuuid is None:
        return 404, {}

    summoner = Summoner.objects.filter(puuid__exact=puuuid)

    if summoner.exists():
        summoner = summoner.first()

        if (timezone.now() - summoner.update_at).days < 3:
            ranked_solo_duo = RankedSoloDuo.objects.get(summoner=summoner)
            ranked_flex = RankedFlex.objects.get(summoner=summoner)

            matches = riot.get_formated_matches_data(summoner)

            return 200, {
                'summoner': summoner,
                'ranked_solo_duo': ranked_solo_duo,
                'ranked_flex': ranked_flex,
                'matches': matches,
            }

    response_data = riot.update_summoner_info(
        region, puuuid, game_name, tag_line
    )

    riot.update_matches_details(response_data['summoner'].puuid)
    matches = riot.get_formated_matches_data(response_data['summoner'].puuid)

    response_data['matches'] = matches

    return 200, response_data


@summoners_router.get(
    '{region}/{game_name}-{tag_line}/update',
    response={200: SummonerInfosOut, 404: dict},
)
def force_update_summoners_infos(
    request: HttpRequest, region: str, game_name: str, tag_line: str
) -> HttpResponse:
    riot = RiotLolApi()

    puuuid = riot.get_puuid_by_riotid(game_name, tag_line)

    if puuuid is None:
        return 404, {}

    response_data = riot.update_summoner_info(
        region, puuuid, game_name, tag_line
    )

    return 200, response_data


@summoners_router.get(
    'matches/{puuid}/update', response={200: List[MatchOut], 404: dict}
)
def update_matches_details(request: HttpRequest, puuid: str) -> HttpResponse:
    riot = RiotLolApi()

    summoner = Summoner.objects.filter(puuid=puuid)
    print(summoner)
    # riot.update_matches_details(puuid)
    matches = riot.get_formated_matches_data(summoner)
    print(matches)
    return 200, matches
