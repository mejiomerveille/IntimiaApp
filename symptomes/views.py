from django.shortcuts import render, redirect
# Create your views here.
from .models import Symptome
from .forms import SymptomeForm
from grossesse.models import Grossesse
from django.contrib.auth.models import User

def enregistrer_symptome(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):
        if request.method == 'POST':
            form = SymptomeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('liste_symptomes')
        else:
            form = SymptomeForm()
        return render(request, 'symptomes/enregistrer_symptome.html', {'form': form})

def liste_symptomes(request):
    symptomes = Symptome.objects.all()
    return render(request, 'symptomes/liste_symptomes.html', {'symptomes': symptomes})
