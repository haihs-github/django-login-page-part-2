
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sigin/', views.sigin, name='sigin'),
    path('sigin/checklogin', views.checklogin, name='checklogin')
]
