from django.conf.urls import url
from django.shortcuts import redirect
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
# JBA - had to change the url for the main landing as it was not catching the redirect for some reason.
	# url(r'^$', redirect('/main')),
	url(r'^$', views.Main.as_view(), name='brr-landing'),
	url(r'^login/$', views.Login.as_view(), name='brr-login'),
	url(r'^register/$', views.Register.as_view(), name='brr-register'),
	url(r'^dashboard/$', views.Dashboard.as_view(), name='brr-dashboard'),
	url(r'^venue/$', views.VenueIndex.as_view(), name='brr-venueindex'),
	url(r'^venue/(?P<venue_id>\d+)', views.Venue.as_view(), name='brr-venue'),
	url(r'^artist/$', views.ArtistIndex.as_view(), name='brr-artistindex'),
	url(r'^artist/(?P<artist_id>\d+)', views.Artist.as_view(), name='bbr-artist'),
]
