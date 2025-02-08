from django.urls import path 
from . import views


urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('user/', views.HelloUserView.as_view(), name='user'),
    path('generate_drill/', views.GenerateDrillView.as_view(), name='generate_drill'),
    path('check_answer/', views.CheckAnswerView.as_view(), name='check_answer'),
]