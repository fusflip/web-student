from django.urls import path

from back import views

urlpatterns = [
    path('', views.index, name='index'),
]