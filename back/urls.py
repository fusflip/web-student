from django.urls import path

from back import views

urlpatterns = [
    path('', views.index, name='index'),
	path('login', views.signIn, name='login'),
	path('profil', views.profil, name='profil'),
	path('discipline', views.discipline, name='discipline'),
	path('discipline_change', views.discipline_change, name='discipline_change'),
	path('registration', views.registration, name='registration'),
]

