from django.contrib import admin
from concert.models import ConcertModel


class ConcertModelAdmin(admin.ModelAdmin):
    list_display = ('concertId','concertName')

admin.site.register(ConcertModel,ConcertModelAdmin)
