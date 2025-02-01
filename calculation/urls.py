from django.urls import path 
from . import views

urlpatterns = [
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('user/', views.HelloUserView.as_view(), name='user'),
]
