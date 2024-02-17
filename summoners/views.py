from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from riot import RiotLolApi
from .models import Summoner, RankedSoloDuo, RankedFlex


def summoner(
    request: HttpRequest, region, game_name, tag_line
) -> HttpResponse:
    if request.method == 'GET':
        riot = RiotLolApi()

        puuuid = riot.get_puuid_by_riotid(game_name, tag_line)

        if puuuid is None:
            return render(request, 'summoner.html')

        summoner = Summoner.objects.filter(puuid__exact=puuuid)

        if summoner.exists():
            summoner = summoner.first()
            ranked_solo_duo = RankedSoloDuo.objects.get(summoner=summoner)
            ranked_flex = RankedFlex.objects.get(summoner=summoner)

            return render(
                request,
                'summoner.html',
                {
                    'summoner': summoner,
                    'ranked_solo_duo': ranked_solo_duo,
                    'ranked_flex': ranked_flex,
                },
            )

        summoner = riot.get_summoner_by_puuid(puuuid, region)

        summoner = Summoner(
            id=summoner.get('id'),
            puuid=summoner.get('puuid'),
            account_id=summoner.get('accountId'),
            name=summoner.get('name'),  # Old game name system
            game_name=game_name,
            tag_line=tag_line,
            profile_icon_id=summoner.get('profileIconId'),
            level=summoner.get('summonerLevel'),
        )

        summoner.save()

        ranked_solo_duo, ranked_flex = riot.get_rankeds_infos_by_summoner_id(
            summoner.id, region
        )

        if ranked_solo_duo:
            ranked_solo_duo = RankedSoloDuo(
                summoner=summoner,
                tier=ranked_solo_duo.get('tier'),
                rank=ranked_solo_duo.get('rank'),
                pdls=ranked_solo_duo.get('leaguePoints'),
                wins=ranked_solo_duo.get('wins'),
                losses=ranked_solo_duo.get('losses'),
            )
        else:
            ranked_solo_duo = RankedSoloDuo(
                summoner=summoner,
            )

        ranked_solo_duo.save()

        if ranked_flex:
            ranked_flex = RankedFlex(
                summoner=summoner,
                tier=ranked_flex.get('tier'),
                rank=ranked_flex.get('rank'),
                pdls=ranked_flex.get('leaguePoints'),
                wins=ranked_flex.get('wins'),
                losses=ranked_flex.get('losses'),
            )
        else:
            ranked_flex = RankedFlex(
                summoner=summoner,
            )

        ranked_flex.save()

        return render(
            request,
            'summoner.html',
            {
                'summoner': summoner,
                'ranked_solo_duo': ranked_solo_duo,
                'ranked_flex': ranked_flex,
            },
        )
