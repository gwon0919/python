from myvote import views
from django.urls import path


urlpatterns = [
    path('', views.DispFunc, name='disp'),  # gogo/ 요청시 
    path('<int:question_id>', views.DetailFunc, name='detail'),       # 인자 컴버터 <type : name>      gogo/1or2
    path('<int:question_id>/vote/', views.VoteFunc, name='vote'),   # gogo/1/vote
    path('<int:question_id>/results',views.ResultFunc, name='results'), 
]
