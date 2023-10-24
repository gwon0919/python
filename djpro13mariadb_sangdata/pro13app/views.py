from django.shortcuts import render, redirect
import MySQLdb
from pro13app.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    return render(request, 'main.html')

def ListFunc(request):
    '''
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from sangdata"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)    # (1, '장갑', 3, 10000), (2, '클렌징티슈', 15, 12000), ...
        print(type(datas)) # <class 'tuple'>
        
        return render(request, 'list.html', {'datas':datas})
    except Exception as err:
        print('Error : ', err)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        '''
    # 페이징을 안한 경우
    # datas = Sangdata.objects.all()
    # print(datas)                                # <QuerySet [<Sangdata: Sangdata object (1)>, ...
    # print(type(datas))                      # <class 'django.db.models.query.QuerySet'>
    # return render(request, 'list.html', {'datas':datas})
    
    # 페이징을 한 경우
    datas = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(datas, 5)     # 페이지 당 5행 씩 출력
    # print(paginator)
    try:
        page = request.GET.get('page')
    except  :
        page = 1
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger :
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages()) 
    
    # 개별 페이지 표시 작업용
    allpage = range(paginator.num_pages + 1)
    print('allpage : ' , allpage)
    return render(request, 'list2.html', {'datas':data, 'allpage': allpage})
    
def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == "POST":
        code = request.POST.get("code")
        # 새 상품 code 유무 검증 후 isnert 진행
        try:
            Sangdata.objects.get(code=code)
            return render(request,'insert.html', {'msg':'이미 등록된 번호입니다.'})
        except Exception  :
            # 추가 작업
            Sangdata(
                code = code,
                sang = request.POST.get("sang"),
                su = request.POST.get("su"),
                dan = request.POST.get("dan")
                ).save()
            return HttpResponseRedirect("/sangpum/list")
        

def UpdateFunc(request):
    updata = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'data': updata})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRecord = Sangdata.objects.get(code=request.POST.get("code"))
        upRecord.code = request.POST.get("code")
        upRecord.sang = request.POST.get("sang")
        upRecord.su = request.POST.get("su")
        upRecord.dan = request.POST.get("dan")
        upRecord.save()
        return redirect('/sangpum/list')

def DeleteFunc(request):
    delRecord = Sangdata.objects.get(code=request.GET.get("code"))
    delRecord.delete()
    return redirect('/sangpum/list')












