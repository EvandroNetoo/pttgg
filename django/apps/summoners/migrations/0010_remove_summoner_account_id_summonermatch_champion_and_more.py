# Generated by Django 5.0.2 on 2024-02-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'summoners',
            '0009_summonermatch_win_alter_match_queue_type_and_more',
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summoner',
            name='account_id',
        ),
        migrations.AddField(
            model_name='summonermatch',
            name='champion',
            field=models.CharField(default='Yasuo', max_length=50),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='profile_icon_id',
            field=models.IntegerField(default=29),
        ),
    ]
