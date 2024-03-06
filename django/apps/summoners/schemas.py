from typing import Dict, List
from ninja import Schema, ModelSchema
from summoners.models import Summoner, Ranked, Match, SummonerMatch


class SummonerOut(ModelSchema):
    class Meta:
        model = Summoner
        fields = [
            'puuid',
            'game_name',
            'tag_line',
            'name',
            'profile_icon_id',
            'level',
        ]

    icon_url: str


class RankedOut(ModelSchema):
    class Meta:
        model = Ranked
        fields = [
            'tier',
            'rank',
            'pdls',
            'wins',
            'losses',
        ]

    win_rate: int
    ranked_emblem: str


class SummonerMatchOut(ModelSchema):
    class Meta:
        model = SummonerMatch
        exclude = ['id', 'match']

    summoner: SummonerOut
    cs_p_min: str
    item_image_url: str


class MatchOut(ModelSchema):
    class Meta:
        model = Match
        exclude = ['id', 'queue_id']

    teams: Dict[str, List[SummonerMatchOut]]


class SummonerInfosOut(Schema):
    summoner: SummonerOut
    ranked_solo_duo: RankedOut
    ranked_flex: RankedOut
    matches: List[MatchOut]
