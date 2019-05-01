from django.shortcuts import render
from rest_framework import viewsets
from .models import stats,teaminfo,teamplayers
from .serializers import StatsSerializer
from django.http import HttpResponse
from .search import statsDocument
from elasticsearch_dsl.query import Q
# Create your views here.
#class StatsView(viewsets.ModelViewSet):
#	queryset=stats.objects.all().filter(team="ATL")
#	serializer_class=StatsSerializer

# way to write sql queries
#def homepage(request):
#	#return HttpResponse('homepage.html')
#	posts=stats.objects.raw('select * from nba_games_stats where team="ATL"')
#	args={'posts':posts}
#	return render(request,'test.html',args)

def test(request):
	getteamcode="BOS"
	yearwin=stats.objects.raw('select id, count(*) as total,(select count(*) as win from nba_games_stats where team=%s and winorloss="W" and year(date)=2014) as win2014, (select count(*) as win from nba_games_stats where team=%s and winorloss="W" and year(date)=2015) as win2015, (select count(*) as win from nba_games_stats where team=%s and winorloss="W" and year(date)=2016) as win2016, (select count(*) as win from nba_games_stats where team=%s and winorloss="W" and year(date)=2017) as win2017, (select count(*) as win from nba_games_stats where team=%s and winorloss="W" and year(date)=2018) as win2018 from nba_games_stats',params=[getteamcode,getteamcode,getteamcode,getteamcode,getteamcode])
	args={'winorlose':yearwin}
	return render(request,'test.html',args)


def search(request):
	searchby=request.GET.get('q')
	if searchby:
		posts=statsDocument.search().query(Q("match",teamcode=searchby)|Q("match",teamname=searchby))
		getteamname=""
		getteamcode="ATL"
		if posts!='':
			for post in posts:
				getteamname=post.teamname
				getteamcode=post.teamcode
			players=teamplayers.objects.all().filter(team_name=getteamname)
			winorlose=stats.objects.raw('select id, count(*) as total,(select count(*) from nba_games_stats where winorloss="W" and team=%s) as win,(select count(*) from nba_games_stats where winorloss="L" and team=%s) as lose from nba_games_stats where team=%s',params=[getteamcode,getteamcode,getteamcode])
			yearwin=stats.objects.raw( 'select id, count(*), (select count(*)from nba_games_stats where team=%s and winorloss="W" and (year(date)=2014 and month(date)>9 or year(date)=2015 and month(date)<6)) as win2014, (select count(*)from nba_games_stats where team=%s and winorloss="W" and (year(date)=2015 and month(date)>9 or year(date)=2016 and month(date)<6)) as win2015, (select count(*)from nba_games_stats where team=%s and winorloss="W" and (year(date)=2016 and month(date)>9 or year(date)=2017 and month(date)<6)) as win2016, (select count(*)from nba_games_stats where team=%s and winorloss="W" and (year(date)=2017 and month(date)>9 or year(date)=2018 and month(date)<6)) as win2017 from nba_games_stats;',params=[getteamcode,getteamcode,getteamcode,getteamcode])
			teampointavg=stats.objects.raw( 'select id, count(*), (select avg(teampoints)from nba_games_stats where team=%s and (year(date)=2014 and month(date)>9 or year(date)=2015 and month(date)<6)) as avg2014, (select avg(teampoints)from nba_games_stats where team=%s and (year(date)=2015 and month(date)>9 or year(date)=2016 and month(date)<6)) as avg2015, (select avg(teampoints)from nba_games_stats where team=%s and (year(date)=2016 and month(date)>9 or year(date)=2017 and month(date)<6)) as avg2016, (select avg(teampoints)from nba_games_stats where team=%s and (year(date)=2017 and month(date)>9 or year(date)=2018 and month(date)<6)) as avg2017 from nba_games_stats;',params=[getteamcode,getteamcode,getteamcode,getteamcode])
		else:
			players=''
			winorlose=''
			teampointavg=''
	else:
		posts=''
		players=''
		winorlose=''
		yearwin=''
		teampointavg=''
	return render(request, 'index.html', {'posts':posts,'players':players,'winorlose':winorlose,'yearwin':yearwin,'teampointavg':teampointavg})

def allteams(request):
	posts=''
	return render(request, 'teams.html', {'posts':posts})

def data(request):
	posts=''
	return render(request, 'data.html', {'posts':posts})

def about(request):
	posts=''
	return render(request, 'about.html', {'posts':posts})