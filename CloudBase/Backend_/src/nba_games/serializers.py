from rest_framework import serializers
from .models import stats

class StatsSerializer(serializers.ModelSerializer):
	class Meta:
		model = stats
		fields = ('team', 'game','date', 'home','opponent','winorloss','teampoints','opponentpoints','fieldgoals','fieldgoalsattempted','fieldgoalspercent','x3pointshots','x3pointshotsattempted','x3pointshotspercent','freethrows','freethrowsattempted','freethrowspercent','offrebounds','totalrebounds','assists','steals','blocks','turnovers','totalfouls','oppfieldgoals','oppfieldgoalsattempted','oppfieldgoalspercent','opp3pointshots','opp3pointshotsattempted','opp3pointshotspercent','oppfreethrows','oppfreethrowsattempted','oppfreethrowspercent','oppoffrebounds','opptotalrebounds','oppassists','oppsteals','oppblocks','oppturnovers','opptotalfouls')
		
