from django.conf.urls import url
from .import views


urlpatterns = [
    # /s_club/
    url(r'^$', views.index , name='index'),
    # /s-clubs/club_id/
    url(r'^(?P<club_id>[0-9])/$', views.details, name='club_detail'),

   #/s-clubs/club/add
    url(r'club/add/$', views.ClubCreate.as_view(), name='create-club')

]
