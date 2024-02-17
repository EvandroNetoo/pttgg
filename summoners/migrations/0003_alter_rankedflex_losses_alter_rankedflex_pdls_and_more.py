# Generated by Django 5.0.2 on 2024-02-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoners', '0002_alter_rankedflex_rank_alter_rankedsoloduo_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankedflex',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rankedflex',
            name='pdls',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rankedflex',
            name='rank',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='rankedflex',
            name='tier',
            field=models.CharField(default='UNRANKED', max_length=10),
        ),
        migrations.AlterField(
            model_name='rankedflex',
            name='wins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='pdls',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='rank',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='tier',
            field=models.CharField(default='UNRANKED', max_length=10),
        ),
        migrations.AlterField(
            model_name='rankedsoloduo',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]