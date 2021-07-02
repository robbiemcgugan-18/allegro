from django.contrib import admin
from allegro.models import UserProfile, Music, Event, PartFormat, Request

admin.site.register(UserProfile)
admin.site.register(Music)
admin.site.register(Event)
admin.site.register(PartFormat)
admin.site.register(Request)
