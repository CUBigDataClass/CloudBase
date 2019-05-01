
from django.contrib import admin
from django.urls import path, include
from nba_games import views
urlpatterns = [
	path('', views.search),
	path('team/', views.allteams),
	path('data/', views.data),
	path('about/', views.about),
	path('test/',views.test),
    path('admin/', admin.site.urls),

	#path('',views.test),
	#path('index/', )
]
