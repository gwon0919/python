from django.shortcuts import render
from pro9app.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    datas = Article.objects.all()
    return render(request, 'list.html', {'datas':datas})
    