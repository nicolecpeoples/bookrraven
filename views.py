from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
class Main(View):
	logform = AuthenticationForm
	regform = UserCreationForm
	def get(self, request):
		context = {
			'logform': self.logform,
			'regform': self.regfom,
		}
		return render(request, 'bookrraven/landing.html', context)

class Login(View):
	logform = AuthenticationForm(request.POST)
	regform = UserCreationForm
	def post(self, request):
		context = {
			'logform': self.logform,
			'regform': self.regform,
		}
		if self.logform.is_valid():
			username = self.logform.cleaned_data['username']
			password = self.logform.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/dashboard/')
			else:
				context = {
					'logform': self.logform,
					'regform': self.regform,
				}
				return render(request, 'bookrraven/landing.html', context)
		else:
			return render(request, 'bookrraven/landing.html', context)

class Register(View):
	logform = AuthenticationForm
	regform = UserCreationForm(request.POST)
	def post(self, request):
		# for errors
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
		if (artist):
			artistInfo = 
			context = {
				'artistInfo': artistInfo,
			}
			return render(request, 'bookrraven/artisthome.html', context)
		else:
			# get booker informations
			bookerinfo = getBookerInfo(request.POST.username)
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
class Venue(View):
	def get(self,request):
		venueInfo = 
		eventList = 
		context = {
			'eventList': eventList,
			'venueInfo': venueInfo,
		}
		return render(request, 'bookrraven/venue.html', context)
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

	def getArtistInfo(self, request):
		# get artists info for profile page
		pass

