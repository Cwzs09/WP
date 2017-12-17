from django.conf.urls import url
from .import views

urlpatterns = [
    # /events/
    url(r'^$', views.index , name='index'),
    # /events/club_id/
    url(r'^(?P<event_id>[0-9])/$', views.detail, name='event_detail'),
]