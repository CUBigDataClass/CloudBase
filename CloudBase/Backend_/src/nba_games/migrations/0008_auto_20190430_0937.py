# Generated by Django 2.1.7 on 2019-04-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_games', '0007_auto_20190429_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='championships',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='retired_numbers',
            field=models.IntegerField(null=True),
        ),
    ]
