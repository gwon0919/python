from django.shortcuts import render
from django.http.response import HttpResponse
from dask.array.random import randint

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
        i = randint(1,100)
        if i % 2 == 0:
            gen = "남자"
            img = "/static/images/sul.jpg"
        else:
            gen = "여자"
            img = "/static/images/sohee.jpg"
        return render(request, 'show.html', {'gen':gen ,'img': img})
        