from django.http import Http404
from django.shortcuts import render
from Events.models import Event

def index(request):
    all_events = Event.objects.all()
    return render(request, 'Events/index.html', {'all_events': all_events})


def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'Events/detail.html', {'event': event})
