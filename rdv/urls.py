from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('ajouter/', views.ajouter_rendezvous, name='ajouter_rendezvous'),
    path('questions/', views.afficher_questions, name='questions'),
]