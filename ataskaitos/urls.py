from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    # path('', views.base, name='base'),
    # path('report/', views.base, name='base'),
    path('register/', views.register, name='register'),
]