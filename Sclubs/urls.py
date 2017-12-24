from django.conf.urls import url, include
from .import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # /s_club/
    url(r'^$', views.index , name='index'),
    # /s-clubs/club_id/
    url(r'^(?P<club_id>[0-9])/$', views.details, name='club_detail'),



]

urlpatterns += [
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^logout/$', views.logout_view, name='logout'),
  url(r'^login/$', views.login_view, name='login'),
]


