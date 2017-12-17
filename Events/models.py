from __future__ import unicode_literals
from django.db import models
from Sclubs.models import Club

class Event(models.Model):
    Event_Name = models.CharField(max_length=200)
    Event_Date = models.DateTimeField()
    Description = models.CharField(max_length=1000, blank=True ,null=True)
    Event_venue = models.CharField(max_length=200, blank=True ,null=True)
    Event_Poster = models.CharField(max_length=1000, blank=True ,null=True)
    Event_Speaker= models.CharField(max_length=200, blank=True ,null=True)
    Organizer_Club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.Event_Name