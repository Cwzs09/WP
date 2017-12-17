from django.contrib import admin
from Sclubs.models import University,Club,Member
from Events.models import Event

admin.site.register(University)
admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Event)