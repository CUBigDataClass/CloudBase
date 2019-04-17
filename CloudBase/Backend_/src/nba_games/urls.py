from django.urls import path, include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('stats',views.StatsView)

urlpatterns=[
	path('home/',include(router.urls))
	
]