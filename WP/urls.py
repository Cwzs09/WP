from django.conf.urls import include , url
from django.contrib import admin

urlpatterns = [
    # /admin/
    url(r'^admin/', admin.site.urls),
    # /s-clubs/
    url(r'^s-clubs/', include('Sclubs.urls')),
    # /events/
    url(r'^events/', include('Events.urls')),
]

