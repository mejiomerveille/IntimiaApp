from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from grossesse.models import Grossesse
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Note

def get_notes(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):
        notes = Note.objects.all()
        data = []
        for note in notes:
            data.append({
                'titre': note.titre,
                'objet': note.objet,
                'date_added': note.date_added.strftime("%Y-%m-%d %H:%M:%S")
            })
        return JsonResponse(data, safe=False)

def note_list(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):
        notes = Note.objects.all()
        return render(request, 'note/note_list.html', {'notes': notes})
    return render(request,'chats/404.html')


def create_note(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):  
        if request.method == 'POST':
            form = NoteForm(request.POST)
            grossesse_id = Grossesse.objects.first()

            if form.is_valid():
                note = form.save(commit=False)
                note.grossesse_id = grossesse_id
                note.save()
                return redirect('note_list')
        else:
            form = NoteForm()
        return render(request, 'note/create_note.html', {'form': form})
    return render(request,'chats/404.html')
    

def edit_note(request, note_id):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):
        note = Note.objects.get(id=note_id)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('note_list')
        else:
            form = NoteForm(instance=note)
        return render(request, 'note/edit_note.html', {'form': form, 'note': note})
    return render(request,'chats/404.html')
    


def delete_note(request, note_id):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if(grossesse):
        note = Note.objects.get(id=note_id)
        if request.method == 'POST':
            note.delete()
            return redirect('note_list')
        return render(request, 'note/delete_note.html', {'note': note})
    return render(request,'chats/404.html')
    