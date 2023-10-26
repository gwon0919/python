from django.urls import path
from pro14app import views


urlpatterns = [
    path('jiklist', views.JikwonFunc),
    path('goList', views.GogekFunc),  
    
]
