# Generated by Django 2.1.7 on 2019-04-30 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_games', '0008_auto_20190430_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='teamplayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20, null=True)),
                ('team_name', models.CharField(max_length=50, null=True)),
                ('player', models.CharField(max_length=50, null=True)),
                ('jersey', models.CharField(max_length=10, null=True)),
                ('position', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
                ('birthday', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('age', models.IntegerField(null=True)),
                ('experience', models.CharField(max_length=10, null=True)),
                ('school', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
