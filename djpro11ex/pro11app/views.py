from django.shortcuts import render, redirect
from pro11app.models import Familydb

# Create your views here.
def ListFunc(request):
    fdatas = Familydb.objects.all()
    return render(request,'list.html',{'fdatas':fdatas})

def InsertFunc(request):
    return render(request,'main.html')

def InsertOkFunc(request):
    if request.method == "POST":
        Familydb(
            name = request.POST.get('name'),
            nai = request.POST.get('nai'),
            tel = request.POST.get('tel'),
            gen = request.POST.get('gen'),
            ).save()
    return redirect("/select")