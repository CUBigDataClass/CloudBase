from django.shortcuts import render
from rest_framework import viewsets
from .models import stats,teaminfo
from .serializers import StatsSerializer
from django.http import HttpResponse
from .search import statsDocument
from elasticsearch_dsl.query import Q
# Create your views here.
class StatsView(viewsets.ModelViewSet):
	queryset=stats.objects.all().filter(team="ATL")
	serializer_class=StatsSerializer

# way to write sql queries
def homepage(request):
	#return HttpResponse('homepage.html')
	posts=stats.objects.raw('select * from nba_games_stats where team="ATL"')
	args={'posts':posts}
	return render(request,'test.html',args)

def test(request):
	posts=stats.objects.raw('select id, count(*) as k, team from nba_games_stats group by team')
	args={'posts':posts}
	return render(request,'index.html',args)


def search(request):
	searchby=request.GET.get('q')
	if searchby:
		posts=statsDocument.search().query(Q("match",teamcode=searchby)|Q("match",teamname=searchby))

	else:
		posts=''
	return render(request, 'index.html', {'posts':posts})