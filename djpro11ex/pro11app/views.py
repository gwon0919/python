from django.shortcuts import render, redirect
from pro11app.models import Familydb

# Create your views here.
def ListFunc(request):
    fdatas = Familydb.objects.all()
    total = len(fdatas)
    sum_age = sum(int(f.nai) for f in fdatas)
    avg_age = sum_age / total if total > 0 else 0
    return render(request,'list.html', {'fdatas':fdatas,'total':total, 'avg_age':avg_age})

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