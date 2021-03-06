# Generated by Django 2.1.7 on 2019-04-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_games', '0006_remove_teaminfo_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='arena',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='g_league',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='general_manager',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='head_coach',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='owner',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
