from django.db import models
from django.templatetags.static import static


class Summoner(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=47)
    puuid = models.CharField(unique=True, max_length=78)
    account_id = models.CharField(unique=True, max_length=56)

    name = models.CharField(max_length=16, blank=True)  # Old game name system
    game_name = models.CharField(max_length=16)
    tag_line = models.CharField(max_length=5)

    profile_icon_id = models.IntegerField()
    level = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.game_name} #{self.tag_line}'


class Ranked(models.Model):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10, default='UNRANKED')
    rank = models.CharField(max_length=3, default='')
    pdls = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    highs_tier = ['MASTER', 'GRANDMASTER', 'CHALLENGER']

    @property
    def win_rate(self):
        if (0, 0) == (self.wins, self.losses):
            return 0
        return int(self.wins / (self.wins + self.losses) * 100)

    @property
    def ranked_emblem(self):
        return static(f'ranked_emblems/{self.tier}.png')

    def __str__(self) -> str:
        return f'{self.summoner} | {self.tier} {self.rank} {self.pdls} pdls'

    class Meta:
        abstract = True


class RankedSoloDuo(Ranked):
    pass


class RankedFlex(Ranked):
    pass
