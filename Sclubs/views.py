from django.http import Http404
from django.shortcuts import render
from Sclubs.models import Club

def index(request):
    all_clubs = Club.objects.all()
    return render(request, 'Sclubs/index.html', {'all_clubs': all_clubs,})


def details(request, club_id):
    try:
        club = Club.objects.get(pk=club_id)
    except Club.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'Sclubs/detail.html', {'club': club})
