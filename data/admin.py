from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportActionModelAdmin
from data.models import fuyuzhe, zhihu, guxiaobei, news, tempnews, SiteMap
from data.views import siteMapview

admin.AdminSite.site_header = 'Devops增益系统'
admin.AdminSite.site_title = 'Devops增益系统'
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(news)
class newsAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link_url','type','createddate')
    search_fields = ('title',)
    list_filter = ('type',)
    list_per_page = 20

@admin.register(tempnews)
class tempnewsAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link_url','type','createddate')
    search_fields = ('title',)
    list_filter = ('type',)
    list_per_page = 20

@admin.register(fuyuzhe)
class fuyuzheAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link_url','subtype','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype','checked',)
    list_editable = ('checked', )
    # list_display_links = ('title',)
    list_per_page = 50
    # ordering = ('title',)

@admin.register(guxiaobei)
class guxiaobeiAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link_url','subtype','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype','checked',)
    list_editable = ('checked', )
    list_per_page = 50
    # ordering = ('title',)

@admin.register(zhihu)
class zhihuAdmin(ImportExportActionModelAdmin):
    list_display = ('itemid','title','link_url','subtype','star','sent','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype',)
    list_display_links = ('itemid',)
    list_editable = ('checked', )
    list_per_page = 20
    ordering = ('-id',)

'''
SiteMap
'''
@admin.register(SiteMap)
class SiteMapAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return siteMapview(request)
