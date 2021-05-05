from django.db import models

from django.utils.html import format_html

'''
HisConsole 监控管理
'''
class Server(models.Model):

    product_choice = (
        ('0', 'Public'),
        ('1', 'CoudTest'),
        ('2', 'Digital'),
        ('4', 'Finance'),
        ('5', 'Service'),
    )  # 类型

    name = models.CharField(verbose_name='主机名', max_length=128)
    ip = models.CharField(verbose_name='IP', max_length=128)
    resource = models.CharField(verbose_name='资源类型', max_length=250,blank=True, null=True)
    product = models.CharField(verbose_name='产品线',choices=product_choice, max_length=250, blank=True, null=True)
    owner = models.CharField(verbose_name='责任人', max_length=50,blank=True, null=True)
    # ontime = models.CharField(verbose_name='启用时间', max_length=200, blank=True, null=True)
    ontime = models.DateField(verbose_name='启用时间', blank=True, null=True)
    offtime = models.DateField(verbose_name='停用时间', blank=True, null=True)

    issynctag = models.BooleanField(verbose_name='是否同步标签', default=False, null=True)
    isactivate = models.BooleanField(verbose_name='是否有效主机', default=True, null=True)

    createddate = models.CharField(verbose_name='createddate', max_length=200, blank=True, null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Server主机"

    def __str__(self):
        return self.name
        # 每行增加执行Job POST按钮
    def post_server(self):
        btn_str = '<input name="重启" onclick="javascript:PostData(\'' + self.ip + '\')" type="button" id="btn_assign" value="重启" class="el-button el-button--small">'
        return format_html(btn_str)
    post_server.short_description = 'Post重启'

    # 每行增加执行Job POST按钮
    def get_server(self):
        btn_str = '<input name="重启" onclick="javascript:GetData(\''+ self.name +'\')" type="button" id="btn_assign" value="重启" class="el-button el-button--primary el-button--small">'
        return format_html(btn_str)
    get_server.short_description = 'Get重启'


class Task(models.Model):
    class WinCharToLinuxField(models.TextField):
        def pre_save(self, model_instance, add):
            current_value = getattr(model_instance, self.attname)
            setattr(model_instance, self.attname, str.replace(current_value,"\r\n","\n"))
            return getattr(model_instance, self.attname)

    type = (
        ('临时脚本', '临时脚本'),
        ('日常运维', '日常运维'),
    )  # 类型
    name = models.CharField(verbose_name='名称', max_length=128)
    type = models.CharField(verbose_name='类型',choices=type, max_length=128, blank=True, null=True)
    cmd = WinCharToLinuxField(verbose_name='命令')
    parameter = models.CharField(verbose_name='参数', max_length=1024, blank=True, null=True)
    isactivate = models.BooleanField(verbose_name='是否有效', default=True, null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200, blank=True, null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200, blank=True, null=True)





    class Meta:
        verbose_name = "task"
        verbose_name_plural = "命令脚本配置"

    def __str__(self):
        return self.name

class DoTask(Task): # 父类为要展示的model类
    class Meta:
        proxy = True
        verbose_name = 'DoTask'
        verbose_name_plural = verbose_name