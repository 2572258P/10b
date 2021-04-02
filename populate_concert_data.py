# -*- coding: utf-8 -*-

import os
import random
from datetime import datetime



# Tell Django where the settings.py module is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'team10b.settings')

import django
django.setup()
from concert.models import ConcertModel,Band,UserProfile
from concert.views import getTimeToInt
from django.contrib.auth.models import User

bandNames = ("Queen","Beatles","Travis","Chvrches","BTS","Metallica","LimpBizkit","Nirvana")
concertNames = ("Live Aid","Bonnaroo","at Reading","Blond Ambition Tour","in Sarajevo","UK Tour","Glasgow's Night","Secret World Tour")
locations = ("Glasgow","London","Seoul","Cyprus","Amsterdam")


test_firstName = "WAD2"
test_lastName = "team10b"
test_email = "team10b@gmail.com"
test_password = "team10b"


def addUser(username):
    username = username
    first_name = test_firstName
    last_name = test_lastName
    email = test_email
    password = test_password
    
    newUser = User.objects.get_or_create(username=username,first_name=first_name,last_name=last_name,email=email)[0]
    newUser.set_password(password)
    newUser.save();
    
    UserProfile.objects.get_or_create(user=newUser,weAreBand=True,uniqueId = getTimeToInt())[0]
    print("User has been created : " + username)
    return newUser

def addBand(user):
        
    bandId = getTimeToInt()
    bandName = bandNames[random.randint(0,len(bandNames)-1 )]
    
    newBand = Band.objects.get_or_create(user=user,
                                         bandId=bandId,
                                         bandName=bandName)[0]        
    newBand.save()
    print("Band has been created : " + bandName)
    return newBand
 
    
    
def addConcert(ownerBand,count):
    print("<Creating Concert>")
    id = getTimeToInt()
    for i in range(count):
        concertId = id+random.getrandbits(16)
        try:
            ConcertModel.objects.get(concertId=concertId)
            continue
        except:        
            concertName = concertNames[random.randint(0, len(concertNames)-1)]
            bandId = ownerBand.bandId
            band = ownerBand
            date = datetime.now()
            location = locations[random.randint(0, len(locations)-1)]
            
            newCon = ConcertModel.objects.get_or_create(concertId=concertId,
                                                        concertName=concertName,
                                                        band=band,
                                                        date=date,
                                                            bandId=bandId,location=location)[0]
            newCon.save()
            print(concertName)

def generateConcertData():    
     #Since adding concert needs a user who has a band, new test user adds each time of running
    user = addUser("team10b_"+str(getTimeToInt()))
    band = addBand(user) #Add a band based on the created user
    addConcert(band,5) #Add concerts with the specified number

# Start execution here!
if __name__ == '__main__':
    print("generate data has begun")
    generateConcertData()