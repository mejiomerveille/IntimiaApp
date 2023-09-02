from django.shortcuts import render
from .models import RendezVous

def accueil(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'accueil.html', {'rendezvous': rendezvous})

def ajouter_rendezvous(request):
    if request.method == 'POST':
        # Logique pour enregistrer les informations du rendez-vous
        pass
    return render(request, 'ajouter_rendezvous.html')

def afficher_questions(request):
    # Logique pour récupérer et afficher les questions
    return render(request, 'questions.html')