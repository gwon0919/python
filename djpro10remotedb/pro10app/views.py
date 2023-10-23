from django.shortcuts import render, redirect
from pro10app.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    print(Guest.objects.filter(title__contains='연습'))
    print(Guest.objects.filter(title='연습'))
    print(Guest.objects.get(id=1))
    
    # select * from pro10app_guest 같은 의미
    gdatas = Guest.objects.all()
    # gdatas = Guest.objects.all().order_by('-id')           # 정렬 방법1
    # gdatas = Guest.objects.all().order_by('title','-id')  # id: descend, title:ascend
    # gdatas = Guest.objects.all().order_by('-id')[0:2]   # 리스트 뽑아내기
    return render(request, 'list.html', {'gdatas': gdatas})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == "POST":
        # print(request.POST.get('title'))
        # print(request.POST['title'])
        # insert into pro10app_guest(...
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()     # supprot python
            # regdate = timezone.now()        # supprot django
        ).save()
            
        # 수정
#        Guest(
#            g = Guest.objects.get(id=수정할번호)
#            g.title = request.POST.get('title'),
#            g.content = request.POST.get('content'),
#        ).save()

        # 삭제
        #g = Guest.objects.get(id=수정할번호)
        #g.delete() 
    # return HttpResponseRedirect("/guest/select")
    return redirect("/guest/select") # 추가 후 목록보기