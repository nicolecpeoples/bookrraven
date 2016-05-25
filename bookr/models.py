from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Users(models.Model):
	BOOKER = 'BKR'
	ARTIST = 'ART'
	ACCESS_CHOICES = (
		(BOOKER, 'Booker'),
		(ARTIST, 'Artist')
		)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	user_phone = models.CharField(max_length=10)
	access = models.CharField(max_length=3, choices=ACCESS_CHOICES)
	hashpass = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Artists(models.Model):
	artist_name = models.CharField(max_length=100)
	site = models.URLField(max_length=200)
	sound = models.URLField(max_length=200)
	artist_photo = models.ImageField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	contact_id = models.ForeignKey('Users')

class Venues(models.Model):
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
	booker_id = models.ForeignKey('Users')

class Events(models.Model):
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
	venue_id = models.ForeignKey('Venues')
	artist_id = models.ForeignKey('Artists')

class Messages(models.Model):
	message = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	event_id = models.ForeignKey('Events')	
	author_id = models.ForeignKey('Users')

class Comments(models.Model):
	comment = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey('Messages')	
	event_id = models.ForeignKey('Events')
	author_id = models.ForeignKey('Users')