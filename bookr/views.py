from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import forms, logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Artist, Venue, Event, Message, Comment

class Main(View):
    def get(self, request):
        logform = forms.AuthenticationForm
        regform = bbrRegForm
        context = {
            'logform': logform,
            'regform': regform,
        }
        return render(request, 'bookrraven/landing.html', context)

class Login(View):
    regform = bbrRegForm
    def post(self, request):
        logform = AuthenticationForm(request.POST)
        context = {
            'logform': logform,
            'regform': self.regform,
        }

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'bookrraven/landing.html', context)

class Register(View):
    logform = AuthenticationForm
    def post(self, request):
        # for errors
        regform = UserCreationForm(request.POST)
        context = {
            'logform': self.logform,
            'regform': regform,
        }
        if regform.is_valid():
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
		item = dir(request.session)
		print (item)
		if request.User.access == 'Artist':
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
		venueList = Venue.objects.all()
		context = {
			'venueList': venueList,
		}
		return render(request, 'bookrraven/venueindex.html', context)
		

class Venues(View):

	def get(self,request, venue_id):
		get_venue = Venue.objects.get(id=venue_id)
		context= {
			'get_venue': get_venue
	def get(self,request):
		venueInfo = Venue.objects.all()
		print(venueInfo)
		context = {
			'venueInfo': venueInfo,

		}
		return render(request, 'bookrraven/venue.html', context)
		

	def getEventList(self, request):
		# get event list info
		pass

class SingleArtist(View):
	def get(self, request, artist_id):
		artistInfo = Artist.objects.get(id = artist_id)
		context = {
			'artistInfo': artistInfo,
		}
		return render(request, 'bookrraven/artistprofile.html', context)

class ArtistIndex(View):
	def get(self,request):

		artistList = Artist.objects.all()
		context = {
			'artistList': artistList,
		}
		return render(request, 'bookrraven/artistindex.html', context)


class Logout(View):
    def get(self,request):
        logout(request, next='/')

# class Test(View):
# 	def get(self, request):
# 		return render(request, 'bookrraven/test.html')