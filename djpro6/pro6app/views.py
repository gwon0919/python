from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")                              # forward 

def selectOsFunc(request):
    # print('request.GET:', request.GET)
    if "favorite_os" in request.GET:
        print(request.GET["favorite_os"])
        request.session["f_os"] = request.GET["favorite_os"] # session key 부여 -> session에 값 저장
        #return HttpResponseRedirect("showos")                  # redirect
        return redirect("/showos")
    else:
        return render(request, "selectos.html")                     # forward
        
def showOsFunc(request):
    # print("showOsFunc 도착")
    dict_context = {}
    
    if "f_os" in request.session:
        print('invaild time: ' , request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]
        dict_context['message'] = "It is %s"%request.session["f_os"]    
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = "You're not choose OS"
    # del request.session["f_os"]     # 특정 키를 가진 세션 삭제
    request.session.set_expiry(5)    # 5초를 주지 않으면 기본 30분    
    
    return render(request, 'show.html', dict_context)