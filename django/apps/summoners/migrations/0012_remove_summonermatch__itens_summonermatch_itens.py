# Generated by Django 5.0.2 on 2024-02-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoners', '0011_alter_summonermatch_champion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summonermatch',
            name='_itens',
        ),
        migrations.AddField(
            model_name='summonermatch',
            name='itens',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]