from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', views.Main.as_view(), name='brr-landing'),
	url(r'^login/$', views.Login.as_view(), name='brr-login'),
	url(r'^register/$', views.Register.as_view(), name='brr-register'),
	url(r'^dashboard/$', views.Dashboard.as_view(), name='brr-dashboard'),
	url(r'^venue/$', views.VenueIndex.as_view(), name='brr-venueindex'),
	url(r'^venue/(?P<venue_id>\d+)', views.Venues.as_view(), name='brr-venue'),
	url(r'^artist/$', views.ArtistIndex.as_view(), name='brr-artistindex'),
	url(r'^artist/(?P<artist_id>\d+)', views.SingleArtist.as_view(), name='bbr-artist'),
	url(r'^logout/', views.Logout.as_view(), name='brr-logout')
	# url(r'^test/$', views.Test.as_view(), name='brr-test')
]
