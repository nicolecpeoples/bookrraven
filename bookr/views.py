from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import forms
from django.contrib.auth import logout
from .models import Artist, Venue
# Create your views here.
class Main(View):
	def get(self, request):
		logform = forms.AuthenticationForm
		regform = forms.UserCreationForm
		context = {
			'logform': logform,
			'regform': regform,
		}
		return render(request, 'bookrraven/landing.html', context)

class Login(View):
	def post(self, request):
		logform = forms.AuthenticationForm(request.POST)
		regform = forms.UserCreationForm
		context = {
			'logform': logform,
			'regform': regform,
		}
		if self.logform.is_valid():
			username = self.logform.cleaned_data['username']
			password = self.logform.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/dashboard')
			else:
				context = {
					'logform': logform,
					'regform': regform,
				}
				return render(request, 'bookrraven/landing.html', context)
		else:
			return render(request, 'bookrraven/landing.html', context)

class Register(View):
	def post(self, request):
		# for errors
		logform = forms.AuthenticationForm
		regform = UserCreationForm(request.POST)
		context = {
			'logform': self.logform,
			'regform': self.regform,
		}
		if self.regform.is_valid():
			regform.save()
			# log 'em in
			user = authenticate(username=regform.cleaned_data['username'], password=regform.cleaned_data['password1'],)
			login(request, user)
			# send them to a dashboard(it'll sort 'em out)
			return redirect('/dashboard/')
		else:
			return render(request, 'bookrraven/landing.html', context)

class Dashboard(View):
	def get(self, request):
		# if our newly logged in user is an artist or booker go to diff sites
		if request.user.groups == 'Artist':
			artistInfo = Artist.objects.get(contact_id=request.user.id)
			context = {
				'artistInfo': artistInfo,
			}
			return render(request, 'bookrraven/artisthome.html', context)
		else:
			# get booker informations
			bookerinfo = Venue.objects.filter(booker_id=request.user.id)
			events = event
			context = {
				'booker_info': bookerinfo,
			} 
			return render(request, 'bookerraven/bookerhome.html', context)

		def getArtistInfo(self, request):
			# gets artist info
			pass

		def getBookerInfo(self,request):
			# gets booker info
			# request_list, event_list, venue_list
			pass

class VenueIndex(View):
	def get(self,request):
		venueList = "SOMETHING"
		context = {
			'venueList': venueList,
		}
		return render(request, 'bookrraven/venueindex.html', context)
		

class Venue(View):
	def get(self,request):
		# venueInfo = 
		# eventList = 
		# context = {
		# 	'eventList': eventList,
		# 	'venueInfo': venueInfo,
		# }
		# return render(request, 'bookrraven/venue.html', context)
		pass

	def getVenueInfo(self, request):
		# get venue info
		pass

	def getEventList(self, request):
		# get event list info
		pass

class Artist(View):
	def get(self, request):
		artistInfo = getArtistInfo()
		context = {
			'artistInfo': artistInfo,
		}
		return render(request, 'bookrraven/artistprofile.html', context)

class ArtistIndex(View):
	def get(self,request):
		artistList = "SOMETHING"
		context = {
			'artistList': artistList,
		}
		return render(request, 'bookrraven/artistindex.html', context)
		pass		

# class Test(View):
# 	def get(self, request):
# 		return render(request, 'bookrraven/test.html')