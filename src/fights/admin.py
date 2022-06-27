from django.contrib import admin

from .models import Fighter, Fight, Vote

admin.site.register(Fighter)
admin.site.register(Fight)
admin.site.register(Vote)
