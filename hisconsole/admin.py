from django.contrib import admin, messages
from import_export.admin import ImportExportActionModelAdmin

from hisconsole.models import Server
from lib.GetJenkinsAPI import get_jobs_data

'''
Server 管理
'''
@admin.register(Server)
class ServerAdmin(ImportExportActionModelAdmin):
    list_display = ('name','ip','resource','product','owner','ontime','offtime','issynctag','isactivate','post_server')
    search_fields = ('ip','name')
    # readonly_fields = ('name','ip','issynctag','isactivate','createddate','updateddate')
    list_filter = ('product', 'owner', 'issynctag', 'ontime', 'offtime')
    list_editable = ('product','owner','ontime', 'offtime')
    list_per_page = 50

    class Media:
        js = ('/static/admin/js/admin/api.js',)

    #屏蔽增加按钮
    def has_add_permission(self, request):
        return False

    #屏蔽删除按钮
    def has_delete_permission(self, request, obj=None):
        return False

    # 增加自定义按钮
    actions = ['synctag']
    def synctag(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            job_list = get_jobs_data() #调用同步标签接口
            server = Server.objects.get(id=id)
            server.issynctag = True
            server.save()
        messages.add_message(request, messages.SUCCESS, '推送成功，推送了{}台主机标签。'.format(len(ids)))
    synctag.short_description = '推送his标签'
    synctag.icon = 'el-icon-s-promotion'

    def syncserver(self, request, queryset):
        hisserver_list = get_jobs_data()
        # servers = Server.objects.all()
        count=0
        for hisserver in hisserver_list:
            try:
                Server.objects.get(name__exact=hisserver["name"])
            except Server.DoesNotExist:
                Server.objects.create(
                    name=hisserver["name"],
                    ip=hisserver["joburl"],
                )
                count = count + 1
        messages.add_message(request, messages.SUCCESS, '刷新成功，新增了{}台主机。'.format(count))
    syncserver.short_description = '拉取his主机'
    syncserver.icon = 'el-icon-s-promotion'



