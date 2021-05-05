from django.contrib import admin, messages
from django.http import JsonResponse
from import_export.admin import ImportExportActionModelAdmin

from devops.password import linuxpassword
from hisconsole.models import Server, Task, DoTask
from hisconsole.shell.paramiko_client import sshBatch
from hisconsole.shell.ssh import SSH
from hisconsole.views import dotaskview
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
    # list_editable = ('product','owner','ontime', 'offtime')
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
    actions = ['exeshell']
    def exeshell(self, request, queryset):
        script = Task.objects.all()
        batchcmd = script.get(name="清理脚本").cmd
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            server = Server.objects.get(id=id)
            try:
                message = ""
                client = SSH(hostname=server.ip, password=linuxpassword)
                for code, out in client.exec_command_with_stream(batchcmd):
                    message += out+"<br/>"
                    print(out)
                server.issynctag = True
                server.save()
                messages.add_message(request, messages.SUCCESS, '执行成功，IP:{}。<br/>{}'.format(server.ip, message))
            except Exception as e:
                message = str(e)
                messages.add_message(request, messages.ERROR, '执行失败，IP:{}。<br/>{}'.format(server.ip, message))
    exeshell.short_description = '执行shell脚本'
    exeshell.icon = 'el-icon-s-promotion'

'''
Task 管理
'''
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','type','cmd','parameter','isactivate')
    search_fields = ('name','cmd')
    list_filter = ('type', )
    list_per_page = 50

'''
DO TASK
'''
# @admin.register(DoTask)
class DoTaskAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return dotaskview(request)

