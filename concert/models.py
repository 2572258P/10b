from django.db import models
from django.contrib.auth.models import User

# Create your models here.

max_char_field = 128 #define another constant when you need another length of string

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pw_confirm = models.CharField(max_length=max_char_field)
    termsOfService = models.BooleanField(default=False)
    weAreBand = models.BooleanField(default=False)
    uniqueId = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class TestModel(models.Model):
    tempId = models.IntegerField(default=0)
    tempName = models.CharField(max_length=max_char_field)

class Band(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bandId = models.IntegerField(default=0)
    bandName = models.CharField(max_length=max_char_field)
    
class ConcertModel(models.Model):    
    concertId = models.IntegerField(default=0)
    concertName = models.CharField(max_length=max_char_field)
    bandId = models.IntegerField(default=0)
    band = models.ForeignKey(Band, on_delete=models.CASCADE,default=0)    
    img = models.ImageField(upload_to='concert_img',blank=True)    
    location = models.CharField(max_length=max_char_field)
    date = models.DateField()
    
class Ticket(models.Model):
    ticketId = models.IntegerField(default=0)
    concertId = models.IntegerField(default=0)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Order(models.Model):
    orderId = models.IntegerField(default=0)
    ticketId = models.IntegerField(default=0)
    bandId = models.IntegerField(default=0)
    