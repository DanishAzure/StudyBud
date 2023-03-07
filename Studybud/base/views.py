from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'python'},
    {'id': 2, 'name': 'Java'},
    {'id': 3, 'name': 'C++'}
]
context = {'rooms': rooms}


def home(request):
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for each_room in rooms:
        if each_room['id'] == int(pk):
            room = each_room

    return render(request, 'base/room.html', {'room': room})
