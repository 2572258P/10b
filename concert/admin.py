from django.contrib import admin
from concert.models import ConcertModel,Band,Ticket,Order,UserProfile


class ConcertModelAdmin(admin.ModelAdmin):
    list_display = ('concertId','concertName','location')


class BandModelAdmin(admin.ModelAdmin):
    list_display = ('bandId','bandName')

class TicketModelAdmin(admin.ModelAdmin):
    list_display = ('ticketId','concertId')

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('orderId','ticketId','bandId')

class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('uniqueId',)


admin.site.register(ConcertModel,ConcertModelAdmin)
admin.site.register(Band,BandModelAdmin)
admin.site.register(Ticket,TicketModelAdmin)
admin.site.register(Order,OrderModelAdmin)
admin.site.register(UserProfile,UserProfileModelAdmin)