from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
# from PIL import Image


class Base_User_Manager(Base_User_Manager):
    def create_user(self, username, password=None):
        newUser = User(username= username, password=password)



class User(AbstractBaseUser):
    BOOKER = 'BKR'
    ARTIST = 'ART'
    ACCESS_CHOICES = (
        (BOOKER, 'Booker'),
        (ARTIST, 'Artist')
        )
    username = models.CharField('Username', max_length=150, unique=True)
    email = models.EmailField('Email Address')
    first_name = models.CharField('First Name', max_length=45)
    last_name = models.CharField('Last Name', max_length=45)
    groups = models.CharField('Access', max_length=3, choices=ACCESS_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = Base_User_Manager()
    def __str__(self):
        return 'ID: %s | Username: %s | Email: %s | Name: %s %s | Access: %s | Pass: %s' % (self.id, self.username, self.email, self.first_name, self.last_name, self.groups, self.password)

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True)
    sound = models.URLField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    artist_photo = models.ImageField(null=True, blank=True, upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_id = models.ForeignKey('User')
    def __str__(self):
        return 'ID: %s | Artist: %s | Main Contact: %s' % (self.id, self.artist_name, self.contact_id.email)

class Venue(models.Model):
	SEATTLE = 'SEA'
	SAN_FRANCISCO = 'SFO'
	CITY_CHOICES = (
		(SEATTLE, 'Seattle'),
		(SAN_FRANCISCO, 'San Francisco')
		)
	WASHINGTON = 'WA'
	CALIFORNIA = 'CA'
	STATE_CHOICES = (
		(WASHINGTON, 'Washington'),
		(CALIFORNIA, 'California')
		)
	venue_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=45, choices=CITY_CHOICES)
	state= models.CharField(max_length=2, choices=STATE_CHOICES)
	zipcode = models.CharField(max_length=5)
	venue_phone = models.CharField(max_length=10)
	venue_photo = models.ImageField(null=True, blank=True, upload_to='uploads/%Y/%m/%d/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	booker_id = models.ForeignKey('User')
	def __str__(self):
		return 'ID: %s | Venue: %s | Booker: %s %s' % (self.id, self.venue_name, self.booker_id.first_name, self.booker_id.last_name)

class Event(models.Model):
	PENDING = 'Pend'
	ACCEPTED = 'Acpt'
	DECLINED = 'Decl'
	STATUS_CHOICES = (
		(PENDING, 'Pending Event'),
		(ACCEPTED, 'Accepted Event'),
		(DECLINED, 'Declined Event')
		)
	event_date = models.DateTimeField()
	status = models.CharField(max_length=45, choices=STATUS_CHOICES, default=PENDING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	venue_id = models.ForeignKey('Venue')
	artist_id = models.ForeignKey('Artist')
	def __str__(self):
		return 'ID: %s | Venue: %s | Artist: %s | Date: %s' % (self.id, self.venue_id.venue_name, self.artist_id.artist_name, self.event_date)

class Message(models.Model):
	message = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	event_id = models.ForeignKey('Event')
	author_id = models.ForeignKey('User')

class Comment(models.Model):
	comment = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey('Message')
	event_id = models.ForeignKey('Event')
	author_id = models.ForeignKey('User')
