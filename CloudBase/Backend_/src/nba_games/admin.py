from django.contrib import admin

# Register your models here.

from .models import stats,teaminfo

admin.site.register(stats)
admin.site.register(teaminfo)
