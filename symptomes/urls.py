from django.urls import path
from symptomes import views

urlpatterns = [
    path('enregistrer_symptome/', views.enregistrer_symptome, name='enregistrer_symptome'),
    path('liste_symptomes/', views.liste_symptomes, name='liste_symptomes'),
]