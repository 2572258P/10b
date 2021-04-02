import os
from django.test import TestCase
from django.urls import reverse
from concert.models import ConcertModel,Band,Ticket
from django.contrib.auth.models import User
from populate_concert_data import generateConcertData

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep} /// {os.linesep} ({os.linesep} /// {os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"



class UrlTest_corresponding_templates(TestCase):
    def test_index_template(self):
        urls = {'concert:index':'concert/index.html',
                'concert:about':'concert/about.html',
                'concert:register':'concert/register.html',
                'concert:signin':'concert/signin.html'}
        
        for url,html in urls.items():
            self.response = self.client.get(reverse(url)) #get a client session no need to require a server
            self.content = self.response.content.decode()
            self.assertTemplateUsed(self.response, html,"Missed html : " + html + f"Header:{FAILURE_HEADER} Footer:{FAILURE_FOOTER}")
            
class Validity_Owner_Check(TestCase):
    def setUp(self):
        generateConcertData();    
    def test_concertOwner(self):
        print("***** Check of validity of concert owners *****")
        concerts = ConcertModel.objects.all();
        for con in concerts:
            print("checking concert : " + con.concertName)
            self.assertEqual(con.band != None,True,"Band is unassigned : " + con.concertName)
            band = Band.objects.filter(bandId=con.bandId)
            self.assertEqual(len(band) > 0,True,"The band does not exist : " + str(con.bandId))            
        print("***** check ended *****")            
    def test_bandOwner(self):
        print("***** Check of validity of band owners *****")
        bands = Band.objects.all();
        for band in bands:
            print("checking band : " + band.bandName)
            self.assertEqual(band.user != None,True,"User is unassigned")
            user = User.objects.filter(username=band.user.username)                
            self.assertEqual(user != None,True,"The user does not exist : "+ band.user.username)        
        print("***** check ended *****")
    def test_bandTicket(self):
        print("***** Check of validity of ticket owners *****")
        tickets = Ticket.objects.all();
        for ticket in tickets:
            print("checking ticket : " + str(ticket.ticketId))
            self.assertEqual(ticket.user != None,True,"User is unassigned")
            user = User.objects.filter(username=ticket.user.username)
            self.assertEqual(user != None,True,"User does not exist",user.username)        
        print("***** check ended *****")
            
            
"""
# Create your tests here.
class concert_unit_test(TestCase):
    def setUp(self):
        generateData()
        self.response = self.client.get(reverse('concert:index'))
        self.content = self.response.content.decode()
        
    def test_ensure_views_are_positive(self):
        orderId = 9
        ticketId = 99
        bandId = 999
        orderTicket = Order(orderId=orderId,ticketId=ticketId,bandId=bandId)
        orderTicket.save()
        self.assertEqual((orderTicket.orderId >= 0), True)
    
    def test_exsitance_of_core_templates(self):
        print()
    def test_exsitance_of_core_templates(self):
        print()
    def test_Concert_Owner_(self):        
        
        
        conAll = ConcertModel.objects.all()
        for con in conAll:
            print(con.concertName)
            
            try:
                band = Band.objects.find(con.band)
            except:
                strMsg = "Not found the band in the concert : " + con.concertName
                self.assert(strMsg)
                
                
"""        