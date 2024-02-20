from ninja import Schema, ModelSchema
from summoners.models import Summoner, Ranked


class SummonerOut(ModelSchema):
    class Meta:
        model = Summoner
        fields = [
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

class SummonerInfosOut(Schema):
    summoner: SummonerOut
    ranked_solo_duo: RankedOut
    ranked_flex: RankedOut