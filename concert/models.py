from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image',blank=True)
    
    def __str__(self):
        return self.user.username


max_char_field = 128 #define another constant when it comes to need more

class TestModel(models.Model):
    tempId = models.IntegerField(default=0)
    tempName = models.CharField(max_length=max_char_field)
    
class ConcertModel(models.Model):
    concertId = models.IntegerField(default=0)
    concertName = models.CharField(max_length=max_char_field)
    bandId = models.IntegerField(default=0)
    location = models.CharField(max_length=max_char_field)
    date = models.DateField()
    tickets = models.IntegerField(default=0)
    
class Band:
    bandId = models.IntegerField(default=0)
    bandName = models.CharField(max_length=max_char_field)
    concertId = models.IntegerField(default=0)
    
class Ticket:
    ticketId = models.IntegerField(default=0)
    concertId = models.IntegerField(default=0)
    userId = models.IntegerField(default=0)
    
    
class Order:
    orderId = models.IntegerField(default=0)
    ticketId = models.IntegerField(default=0)
    bandId = models.IntegerField(default=0)
    