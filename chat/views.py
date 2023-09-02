from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def HomePage(request):
    return render(request, 'app/home.html')

@login_required
def Home(request):
    return render(request, 'app/index.html')