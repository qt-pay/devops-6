from django.shortcuts import render

# Create your views here.
'''
SiteMap moudle
'''
def siteMapview(request):
    return render(request,'admin/quantmap.html')
