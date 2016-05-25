from django.conf.urls import url, pattern
from django.shortcuts import redirect
from . import 
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', redirect('bookrraven')),
	url(r'^bookrraven/$', views.Main.as_view(), name='brr-landing'),
	url(r'^login/$', views.Login.as_view(), name='brr-login'),
	url(r'^register/$', views.Register.as_view(), name='brr-register'),
	url(r'^dashboard/$', login_required(views.Dashboard.as_view()), name='brr-dashboard'),
	url(r'^venue/(?P<venue_id>\d+)', views.Venue.as_view(), name='brr-venue'),
	url(r'^artist/(?P<user_id>\d+)', views.Artist.as_view(), name='bbr-artist'),
]
