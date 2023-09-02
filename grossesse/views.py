from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from grossesse.models import Grossesse
from .forms import GrossesseForm

@login_required
def afficher_calendrier(request):
    grosse: Grossesse = Grossesse.objects.filter(user_id=request.user.id, is_active=True).first()
    id = request.user.id
    print(id)
    if(not grosse):
        # verifier si l'utiisateur a deja une grossesse active
        if request.method == 'POST':
            form=GrossesseForm(request.POST)
            # user_id = User.objects.first()
            if form.is_valid():
                grossesse=form.save(commit=False)  
                grossesse.user_id = request.user
                grossesse.save()
                return render(request, 'grossesse/calendrier.html', {'date_accouchement': grossesse.end_date})
        else:
            form = GrossesseForm()
            content = {
                    'user_id':request.user.id,
                    'form':form,
                }
            return render(request, 'grossesse/calendrier.html', content)
    return render(request,'app/404.html')
    

def principal(request):
    grosse: Grossesse = Grossesse.objects.filter(user_id=request.user.id, is_active=True).first()
    if(grosse):
        if request.method == "GET":
            # recuperer le mois de la grossesse
            user: User = request.user
            print(user)
            grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
            # month = grossesse.start_date.isoformat().split('-')[2]
            today = datetime.now().date()
            date_diff = (today - grossesse.start_date).days // 7
            # faire les difference entre la date actuelle et la date de depart
            list_weeks = list(range(1, 41))

            return render(request, 'grossesse/cadre.html',{'n':list_weeks, 'start_week': date_diff})
    return render(request,'app/404.html')
    
    

def compteur(request):
    if request.method == "GET":
        return render(request, 'grossesse/compteur.html')