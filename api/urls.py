from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlgoResponseView),
    path('getsave', views.ReturnSaveView),
    path('sendmail', views.SendMail)
]