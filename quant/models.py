from django.db import models

# Create your models here.
# Create your models here.
'''
其它实验模块
'''
class Quant(models.Model):
    name = models.CharField(verbose_name='TEST', max_length=128, help_text='TEST')
    class Meta:
        verbose_name = "Quant"
        verbose_name_plural = "Quant"

    def __str__(self):
        return self.name

'''
SiteMap
'''
class SiteMap(Quant):
    class Meta:
        proxy = True
        verbose_name = 'Sitemap'
        verbose_name_plural = verbose_name