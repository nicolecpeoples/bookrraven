from django.contrib import admin

from .models import Artist, Venue, Event

admin.site.register(Artist)
admin.site.register(Venue)
admin.site.register(Event)