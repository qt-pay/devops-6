
from django.shortcuts import render
from app.models import Plantime, Project
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

def TodoChartview(request):
    # res = Todo.objects.values("plantime").annotate(count=Count("plantime")).values("plantime", "count").order_by("plantime")
    res = Plantime.objects.values("name").annotate(count=Count("todo")).values("name", "count")
    resDone = Plantime.objects.values("name").filter(todo__checked__exact=True).annotate(count=Count("todo")).values("name", "count")

    resDevops = Plantime.objects.values("name").filter(todo__project__name__exact="Devops").annotate(
        count=Count("todo")).values("name", "count")
    resOps = Plantime.objects.values("name").filter(todo__project__name__exact="运维Devops").annotate(
        count=Count("todo")).values("name", "count")
    resTrade = Plantime.objects.values("name").filter(todo__project__name__exact="跨境电商").annotate(
        count=Count("todo")).values("name", "count")
    resDatacawl = Plantime.objects.values("name").filter(todo__project__name__exact="数据采集分析").annotate(
        count=Count("todo")).values("name", "count")
    resInvest = Plantime.objects.values("name").filter(todo__project__name__exact="量化投资分析").annotate(
        count=Count("todo")).values("name", "count")
    resPhoto = Plantime.objects.values("name").filter(todo__project__name__exact="摄影后期").annotate(
        count=Count("todo")).values("name", "count")

    resPoject = Project.objects.values("name").annotate(count=Count("todo")).values("name", "count").order_by("-count")
    resPojectDone = Project.objects.values("name").filter(todo__checked__exact=True).annotate(count=Count("todo")).values("name", "count").order_by("-count")

    month = []
    todo = []
    done = []

    devops = []
    ops = []
    trade = []
    invest = []
    datacawl = []
    photo = []

    project = []
    projectCount = []
    projectDoneCount = []

    for index in range(len(res)):
        month.append(res[index]['name'])
        todo.append(res[index]['count'])
        tempDone=tempDevops=tempOps=tempTrade=tempDatacawl=tempPhoto=tempInvest=0
        for indexDone in range(len(resDone)):
            if resDone[indexDone]['name'] == res[index]['name']:
                tempDone=resDone[indexDone]['count']
        done.append(tempDone)

        for indexDevops in range(len(resDevops)):
            if resDevops[indexDevops]['name'] == res[index]['name']:
                tempDevops = resDevops[indexDevops]['count']
        devops.append(tempDevops)
        for indexOps in range(len(resOps)):
            if resOps[indexOps]['name'] == res[index]['name']:
                tempOps = resOps[indexOps]['count']
        ops.append(tempOps)
        for indexTrade in range(len(resTrade)):
            if resTrade[indexTrade]['name'] == res[index]['name']:
                tempTrade = resTrade[indexTrade]['count']
        trade.append(tempTrade)
        for indexInvest in range(len(resInvest)):
            if resInvest[indexInvest]['name'] == res[index]['name']:
                tempInvest = resInvest[indexInvest]['count']
        invest.append(tempInvest)
        for indexDatacawl in range(len(resDatacawl)):
            if resDatacawl[indexDatacawl]['name'] == res[index]['name']:
                tempDatacawl = resDatacawl[indexDatacawl]['count']
        datacawl.append(tempDatacawl)
        for indexPhoto in range(len(resPhoto)):
            if resPhoto[indexPhoto]['name'] == res[index]['name']:
                tempPhoto = resPhoto[indexPhoto]['count']
        photo.append(tempPhoto)

    for index in range(len(resPoject)):
        project.append(resPoject[index]['name'])
        projectCount.append(resPoject[index]['count'])
        tempProjectDone = 0
        for indexDone in range(len(resPojectDone)):
            if resPojectDone[indexDone]['name'] == resPoject[index]['name']:
                tempProjectDone = resPojectDone[indexDone]['count']
        projectDoneCount.append(tempProjectDone)

    context = {'month': month, 'todo': todo, 'done': done,
               'devops': devops,'ops': ops,'trade': trade,'datacawl': datacawl,'photo': photo,'invest': invest,
               'project': project, 'projectCount': projectCount, 'projectDoneCount': projectDoneCount}
    return render(request, 'admin/todoChart.html', context=context)

