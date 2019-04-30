
from django.contrib import admin
from django.urls import path, include
from nba_games import views
urlpatterns = [
	path('', views.search),
	path('search/',views.search, name='search'),
    path('admin/', admin.site.urls),
	path('',views.test),
	#path('index/', )
]
