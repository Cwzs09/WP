from django.conf.urls import include , url
from Sclubs.views import *
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # /admin/
    url(r'^admin/', admin.site.urls),
    # /s-clubs/
    url(r'^s-clubs/', include('Sclubs.urls')),
    # /events/
    url(r'^events/', include('Events.urls')),
]

