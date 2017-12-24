from django.http import Http404
from django.shortcuts import render , redirect
from Sclubs.models import Club
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import  authenticate, login
from django.views.generic import View
from Sclubs.forms import UserForm



def index(request):
    all_clubs = Club.objects.all()
    return render(request, 'Sclubs/index.html', {'all_clubs': all_clubs,})


def details(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except Club.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'Sclubs/detail.html', {'club': club})

class ClubCreate(CreateView):
    model = Club
    fields = ['University','Chairman','Vice_Chairman','Genre','Club_email','Club_Logo','Club_Name']