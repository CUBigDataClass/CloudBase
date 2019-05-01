from django.contrib import admin

# Register your models here.

from .models import stats,teaminfo,teamplayers

admin.site.register(stats)
admin.site.register(teaminfo)
admin.site.register(teamplayers)
