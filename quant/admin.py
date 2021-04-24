from django.contrib import admin

# Register your models here.
from quant.models import SiteMap
from quant.views import siteMapview

'''
SiteMap
'''
@admin.register(SiteMap)
class SiteMapAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return siteMapview(request)