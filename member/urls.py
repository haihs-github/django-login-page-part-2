
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sigin/', views.sigin, name='sigin'),
    path('sigin/checklogin/', views.checklogin, name='checklogin'),
    path('sigout/', views.sigout, name='sigout'),
    path('sigup/', views.sigup, name='sigup'),
    path('sigup/checksigup/', views.checksigup, name='checksigup'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.getedit, name='getedit'),
    path('update/<int:id>', views.update, name='update'),
]
