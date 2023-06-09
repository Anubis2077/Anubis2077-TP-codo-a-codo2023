from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'pages/chatroom.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    mensaje = request.GET.get('mensaje', None)

    return render(request, 'pages/chat.html', {'room': room, 'messages': messages, 'mensaje': mensaje},)