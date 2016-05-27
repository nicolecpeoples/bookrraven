from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime
from PIL import Image


class SomeUser(AbstractBaseUser):
    BOOKER = 'BKR'
    ARTIST = 'ART'
    ACCESS_CHOICES = (
        (BOOKER, 'Booker'),
        (ARTIST, 'Artist')
        )
    email = models.EmailField('Email Address', unique=True, db_index=True)
    first_name = models.CharField('First Name', max_length=45)
    last_name = models.CharField('Last Name', max_length=45)
    groups = models.CharField('Access', max_length=3, choices=ACCESS_CHOICES)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

class People(models.Model):
    BOOKER = 'BKR'
    ARTIST = 'ART'
    ACCESS_CHOICES = (
        (BOOKER, 'Booker'),
        (ARTIST, 'Artist')
        )
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=10)
    access = models.CharField(max_length=3, choices=ACCESS_CHOICES)
    hashpass = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
		return 'ID: %s | Name: %s %s' % (self.id, self.first_name, self.last_name)

class Artist(models.Model):
	artist_name = models.CharField(max_length=100)
	site = models.URLField(max_length=200, blank=True)
	sound = models.URLField(max_length=200, blank=True)
	artist_photo = models.ImageField(upload_to='photo')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	contact_id = models.ForeignKey('People')
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
	venue_photo = models.ImageField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	booker_id = models.ForeignKey('People')
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
	author_id = models.ForeignKey('People')

class Comment(models.Model):
	comment = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey('Message')	
	event_id = models.ForeignKey('Event')
	author_id = models.ForeignKey('People')