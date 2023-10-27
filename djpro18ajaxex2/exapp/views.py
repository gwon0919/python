from django.shortcuts import render
from exapp.models import Producttab
from django.http.response import HttpResponse, JsonResponse
import json
# Create your views here.
def MainFunc(request):
    return render(request,'main.html')

def BurgerFunc(request):
    jdata = Producttab.objects.filter(category=1)
    print(jdata)
    
    datas = []
    # jdata를 dict type으로 저장해 json 형식의 문자열로 클라이언트에 전송
    for j in jdata:
        dicData = {'id' : j.id, 'category' : j.category, 'pname' : j.pname, 'price' : j.price, 'stock' : j.stock, 'description' : j.description}
        datas.append(dicData)
    return HttpResponse(json.dumps(datas),content_type='application/json')

def DrinksFunc(request):
    jdata = Producttab.objects.filter(category=2)
    print(jdata)
    
    datas = []
    # jdata를 dict type으로 저장해 json 형식의 문자열로 클라이언트에 전송
    for j in jdata:
        dicData = {'id' : j.id, 'category' : j.category, 'pname' : j.pname, 'price' : j.price, 'stock' : j.stock, 'description' : j.description}
        datas.append(dicData)
    return HttpResponse(json.dumps(datas),content_type='application/json')

def AdminFunc(request):
    return render(request,'admin.html')

def ListFunc(request):
    ldata = Producttab.objects.all()
    print(ldata)
    
    datas = []
    for l in ldata:
        listData = {'id' : l.id, 'category' : l.category, 'pname' : l.pname, 'price' : l.price, 'stock' : l.stock, 'description' : l.description}
        datas.append(listData)
    return HttpResponse(json.dumps(datas),content_type='application/json')

def InsertFunc(request):
    if request.method == 'GET':
        datas = Producttab.objects.values()
        return JsonResponse(list(datas), safe=False)
    elif request.method == 'POST':
        try:
            new_product = Producttab(
                category=request.POST.get('category'),
                pname=request.POST.get('pname'),
                price=request.POST.get('price'),
                stock=request.POST.get('stock'),
                description=request.POST.get('description'),
            )
            new_product.save()
            return JsonResponse({'message': 'Product added successfully'})
        except Exception as e:
            print('추가 에러 : ', e)
            return JsonResponse({'message': 'Error adding product'}, status=500)

