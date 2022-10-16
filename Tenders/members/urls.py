from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('test/', views.test, name='test'),
   
]