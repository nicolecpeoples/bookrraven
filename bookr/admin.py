from django.contrib import admin

from .models import Artist, Venue, Event, SomeUser

admin.site.register(Artist)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(SomeUser)
