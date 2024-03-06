import json
from django.db import models
from django.templatetags.static import static
from django.utils import timezone


class Summoner(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=47)
    puuid = models.CharField(unique=True, max_length=78)

    name = models.CharField(max_length=16, blank=True)  # Old game name system
    game_name = models.CharField(max_length=16)
    tag_line = models.CharField(max_length=5)

    profile_icon_id = models.IntegerField(default=29)
    level = models.IntegerField(default=1)

    update_at = models.DateTimeField(default=timezone.now)

    @property
    def icon_url(self):
        return f'https://ddragon.leagueoflegends.com/cdn/14.2.1/img/profileicon/{ self.profile_icon_id }.png'

    def __str__(self) -> str:
        return f'{self.game_name} #{self.tag_line}'

    def save(self, *args, **kwargs) -> None:
        self.update_at = timezone.now()

        return super().save(args, kwargs)


class Ranked(models.Model):
    summoner = models.OneToOneField(Summoner, on_delete=models.CASCADE)
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


class Match(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    end_at = models.DateTimeField()
    duration = models.TimeField()
    queue_id = models.IntegerField()
    queue_type = models.CharField(max_length=100)


class SummonerMatch(models.Model):
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()

    gold_earned = models.IntegerField()
    itens = models.JSONField()
    item_image_url = 'https://ddragon.leagueoflegends.com/cdn/14.3.1/img/item/'

    wards_placed = models.IntegerField()
    wards_killed = models.IntegerField()
    vision_wards_bought = models.IntegerField()

    total_damage_dealt = models.IntegerField()
    total_damage_taken = models.IntegerField()

    largest_multi_kill = models.IntegerField()
    level = models.IntegerField()
    creep_strike = models.IntegerField()

    summoner1_id = models.IntegerField()
    summoner2_id = models.IntegerField()

    team_choices = (
        ('B', 'Blue Side'),
        ('R', 'Red Side'),
    )
    team = models.CharField(max_length=1, choices=team_choices)
    win = models.BooleanField()

    champion = models.CharField(max_length=50)

    position_choices = (
        ('TOP', 'TOP'),
        ('JUNGLE', 'JG'),
        ('MIDDLE', 'MID'),
        ('BOTTOM', 'ADC'),
        ('UTILITY', 'UTILITY'),
    )
    position = models.CharField(max_length=7, choices=position_choices)

    def __str__(self) -> str:
        return f'{self.summoner.game_name} #{self.summoner.tag_line} {self.team} {self.position}'

    @property
    def cs_p_min(self) -> str:
        hour_to_minutes = self.match.duration.hour * 60
        seconds_to_minutes = self.match.duration.second / 60
        game_time_in_minutes = (
            hour_to_minutes + self.match.duration.minute + seconds_to_minutes
        )
        return f'{(self.creep_strike / game_time_in_minutes):.1f}'
