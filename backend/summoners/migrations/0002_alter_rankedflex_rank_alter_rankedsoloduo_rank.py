# Generated by Django 5.0.2 on 2024-02-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankedflex',
            name='rank',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='rank',
            field=models.CharField(max_length=3),
        ),
    ]