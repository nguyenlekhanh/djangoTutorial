from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'First room'},
    {'id': 2, 'name': 'Second room'},
    {'id': 3, 'name': 'Third room'},
    {'id': 4, 'name': 'Third room'},
]

def home(request):
    #template = loader.get_template("base/home.html")
    context = {'rooms': rooms};
    return render(request, "base/home.html", context)

def room(request):
    #template = loader.get_template("base/room.html")
    room = None
    context = {'rooms': rooms};
    return render(request, "base/room.html", context)

def room_detail(request, pk):
    #template = loader.get_template("base/room.html")
    room = None
    for i in rooms:
        if i['id']== int(pk):
            room = i

    context = {'room': room}

    return render(request, "base/room_detail.html", context)