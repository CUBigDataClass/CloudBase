from django.shortcuts import render
from rest_framework import viewsets
from .models import stats
from .serializers import StatsSerializer
# Create your views here.

class StatsView(viewsets.ModelViewSet):
	queryset=stats.objects.all().filter(team="ATL")
	serializer_class=StatsSerializer
	