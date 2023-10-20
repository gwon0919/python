from django.shortcuts import render
from pro8app.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    datas = Article.objects.all()   # Django ORM
    print(datas)    # QuerySet type
    print(datas[0].name)
    return render(request, 'list.html', {'datas':datas})
    
    
    