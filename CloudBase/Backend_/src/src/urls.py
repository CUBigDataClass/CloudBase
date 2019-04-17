
from django.contrib import admin
from django.urls import path, include
from nba_games import views

urlpatterns = [
	path('', include('nba_games.urls')),
	path('search/',include('haystack.urls')),
    path('admin/', admin.site.urls),
	path('',views.test),
	#path('index/', )
]
