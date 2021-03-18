from django.contrib import admin
from concert.models import ConcertModel,Band,Ticket,Order


class ConcertModelAdmin(admin.ModelAdmin):
    list_display = ('concertId','concertName','location')


class BandModelAdmin(admin.ModelAdmin):
    list_display = ('bandId','bandName','concertId')

class TicketModelAdmin(admin.ModelAdmin):
    list_display = ('ticketId','concertId','userId')

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('orderId','ticketId','bandId')


admin.site.register(ConcertModel,ConcertModelAdmin)
admin.site.register(Band,BandModelAdmin)
admin.site.register(Ticket,TicketModelAdmin)
admin.site.register(Order,OrderModelAdmin)