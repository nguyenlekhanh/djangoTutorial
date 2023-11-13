from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'First room'},
#     {'id': 2, 'name': 'Second room'},
#     {'id': 3, 'name': 'Third room'},
#     {'id': 4, 'name': 'Third room'},
# ]

def home(request):
    #template = loader.get_template("base/home.html")
    rooms = Room.objects.all();
    context = {'rooms': rooms};
    return render(request, "base/home.html", context)

def room(request):
    #template = loader.get_template("base/room.html")
    room = None
    context = {'rooms': rooms};
    return render(request, "base/room.html", context)

def room_detail(request, pk):
    #template = loader.get_template("base/room.html")
    room = Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, "base/room_detail.html", context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        #print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        #print(request.POST)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}

    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room})