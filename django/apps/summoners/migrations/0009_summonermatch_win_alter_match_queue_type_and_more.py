# Generated by Django 5.0.2 on 2024-02-21 02:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoners', '0008_alter_rankedflex_summoner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='summonermatch',
            name='win',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='queue_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='summonermatch',
            name='position',
            field=models.CharField(
                choices=[
                    ('TOP', 'TOP'),
                    ('JUNGLE', 'JG'),
                    ('MIDDLE', 'MID'),
                    ('BOTTOM', 'ADC'),
                    ('UTILITY', 'SUP'),
                ],
                max_length=7,
            ),
        ),
    ]
