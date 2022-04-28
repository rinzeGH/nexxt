from django.shortcuts import render
from .models import Room, Message
from main.models import Profile


def room_detail(request, room_slug):
    room = Room.objects.prefetch_related('profile').get(slug=room_slug)
    user = request.user
    messages = Message.objects.select_related('profile').filter(room=room)[:25]
    context = {
        'messages': messages,
        'room': room,
        'user': user,
    }
    return render(request, 'room/room_detail.html', context=context)


def room_list(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    rooms = Room.objects.filter(profile=profile).prefetch_related('profile')
    context = {
        'profile_owner': profile,
        'rooms': rooms,
        'user': user,
    }

    return render(request, 'room/room_list.html', context=context)
