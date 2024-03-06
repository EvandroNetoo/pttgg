from django.contrib import admin
from .models import Summoner, RankedSoloDuo, RankedFlex, Match, SummonerMatch

admin.site.register(Summoner)
admin.site.register(RankedSoloDuo)
admin.site.register(RankedFlex)
admin.site.register(Match)
admin.site.register(SummonerMatch)
