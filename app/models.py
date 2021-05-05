from django.db import models

# Create your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe

'''
Devops TODO 系统
'''
class Todo(models.Model):
    todo = models.CharField(verbose_name='IDEA', max_length=128)
    description = models.TextField(verbose_name='描述',  blank=True, null=True)
    project = models.ForeignKey('Project',verbose_name='项目', on_delete=models.CASCADE, blank=True, null=True)
    pior = models.ForeignKey('Pior',verbose_name='优先级', on_delete=models.CASCADE, blank=True, null=True)
    link = models.CharField(verbose_name='link', max_length=500, blank=True, null=True)
    plantime = models.ForeignKey('Plantime',verbose_name='预估时间', on_delete=models.CASCADE, blank=True, null=True)
    checked = models.BooleanField(verbose_name='完成', default=False)
    # tag = models.CharField(verbose_name='标签', max_length=50, blank=True, null=True)
    # startime = models.CharField(verbose_name='开始时间', max_length=200, blank=True, null=True)
    # endtime = models.CharField(verbose_name='结束时间', max_length=200, blank=True, null=True)
    # createddate = models.CharField(verbose_name='createddate', max_length=200, blank=True, null=True)
    # updateddate = models.CharField(verbose_name='updateddate', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "GTD"
        verbose_name_plural = "GTD"

    def __str__(self):
        return self.todo

    def image_data(self):
        imageurl = "/static/red.png"
        if self.checked == True:
            imageurl = "/static/disabled.png"
        elif self.pior.id == 1:
            imageurl = "/static/blue_anime.gif"
        elif self.pior.id == 2:
            imageurl = "/static/blue.png"
        elif self.pior.id == 3:
            imageurl = "/static/nobuilt.png"
        elif self.pior.id == 4:
            imageurl = "/static/health-40to59.png"
        else:
            imageurl = "/static/red.png"
        return mark_safe(u'<img src="%s" style="width: 32px; height: 32px;" />' % imageurl)
    image_data.short_description = u'状态'

    #跳转按钮
    def link_url(self):
        if self.link ==None:
            return ''
        else:
            btn_str = '<a href="{}" target="_blank">{}</a> '
            return format_html(btn_str, self.link, self.link)
    link_url.short_description = 'Url'
#
class Pior(models.Model):
    name = models.CharField(verbose_name='优先级',max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "优先级"
        verbose_name_plural = "优先级"

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(verbose_name='项目',max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"

    def __str__(self):
        return self.name

class Plantime(models.Model):
    name = models.CharField(verbose_name='预估时间',max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "预估时间"
        verbose_name_plural = "预估时间"
    def __str__(self):
        return self.name

class TodoChart(Todo): #
    class Meta:
        proxy = True
        verbose_name = 'GTD趋势图'
        verbose_name_plural = verbose_name


'''
Devops 工具链
'''
class SiteMap(Todo):
    class Meta:
        proxy = True
        verbose_name = 'Sitemap'
        verbose_name_plural = verbose_name

'''
Jenkins 监控管理
'''
class Jenkins(models.Model):
    name = models.CharField(verbose_name='JOB名称', max_length=128)
    joburl = models.CharField(verbose_name='JOB Url', max_length=250,blank=True, null=True)
    description = models.TextField(verbose_name='描述', blank=True, null=True)
    color = models.CharField(verbose_name='图标状态', max_length=25,blank=True, null=True)
    inQueue = models.BooleanField(verbose_name='排队中', default=False, null=True)
    number = models.IntegerField(verbose_name='构建ID',blank=True, null=True)
    result = models.CharField(verbose_name='构建结果', max_length=25,blank=True, null=True)
    buildurl = models.CharField(verbose_name='构建Url', max_length=250,blank=True,null=True)
    building = models.BooleanField(verbose_name='是否构建中', default=False, null=True)
    duration = models.BigIntegerField(verbose_name='耗时(s)',blank=True, null=True)
    estimatedDuration = models.BigIntegerField(verbose_name='预计用时(min)',blank=True , null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200, blank=True, null=True)
    updateddate = models.CharField(verbose_name='刷新时间', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Jenkins"
        verbose_name_plural = "Jenkins"

    def __str__(self):
        return self.name

    def image_data(self):
        imageurl = "/static/red.png"
        if self.inQueue != 0:
            imageurl = "/static/yellow_anime.gif"
        elif self.color == "blue_anime":
            imageurl = "/static/blue_anime.gif"
        elif self.color == "blue":
            imageurl = "/static/blue.png"
        elif self.color == "disabled":
            imageurl = "/static/disabled.png"
        else:
            imageurl = "/static/red.png"
        return mark_safe(u'<img src="%s" style="width: 32px; height: 32px;" />' % imageurl)
    image_data.short_description = u'执行状态'

    #跳转按钮
    def link_job(self):
        btn_str = '<a  href="{}" target="_blank">link </a> '
        return format_html(btn_str, self.joburl)
    link_job.short_description = 'Job Url'

    #每行增加执行Job按钮
    def exec_job(self):
        btn_str = '<a href="{}" target="_blank" rel="external nofollow" >' \
                  '<input name="执行JOB"' \
                      'type="button" class="el-button el-button--button el-button--small" id="execButton" ' \
                  'title="执行JOB" value="执行JOB">' \
                  '</a>'
        return format_html(btn_str, '{}/build?delay=0sec'.format(self.joburl))
    exec_job.short_description = '执行JOB'


'''
其它实验模块
'''
class Money(models.Model):
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    dept = models.CharField(verbose_name='dept', max_length=128,default='dept')
    salary = models.BigIntegerField(verbose_name='金额')
    pay = models.BigIntegerField(verbose_name='金额')
    cost = models.BigIntegerField(verbose_name='金额')
    create_date = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"

    def __str__(self):
        return self.name

class TestControl(Money): # 父类为要展示的model类
    class Meta:
        proxy = True
        verbose_name = 'TestControl'
        verbose_name_plural = verbose_name

class TestChart1(Money): #
    class Meta:
        proxy = True
        verbose_name = 'TestChart1'
        verbose_name_plural = verbose_name

class TestChart2(Money): #
    class Meta:
        proxy = True
        verbose_name = 'TestChart2'
        verbose_name_plural = verbose_name

class ChartByModel(Money): #
    class Meta:
        proxy = True
        verbose_name = 'ChartByModel'
        verbose_name_plural = verbose_name

class ChartBySql(Money): #
    class Meta:
        proxy = True
        verbose_name = 'ChartBySQL'
        verbose_name_plural = verbose_name
