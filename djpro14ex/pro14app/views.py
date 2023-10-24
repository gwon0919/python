from django.shortcuts import render
from pro14app.models import Buser, Jikwon

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
# Create your views here.
def MainFunc(request):
    datas = Buser.objects.all()
    return render(request, 'main.html', {'datas':datas})

def JikFunc(request, buser_num):
    jdatas = Jikwon.objects.filter(buser_num=buser_num).select_related('buser_num')
    return render(request, 'jikList.html', {'jdatas': jdatas})

def GoFunc(requset):
    pass

