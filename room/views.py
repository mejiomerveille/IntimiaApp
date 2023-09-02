from django.shortcuts import render

from .models import *

def rooms(request):
    """ Liste des groupe de chat """
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

def room(request, slug):
    """ Details groupe de chat """
    room = Room.objects.get(slug=slug)    
    messages = Message.objects.filter(room=room)[0:30]
    return render(request, 'room/room.html', {'room': room, 'messages':messages})

    