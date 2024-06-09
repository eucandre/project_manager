from django.db import models
from app_user.models import User
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class Organ(models.Model):
    name = models.CharField(max_length=255,  null=False, blank=False)
    cep = models.CharField(max_length=255,  null=True, blank=True)
    address = models.CharField(max_length=255,  null=True, blank=True)
    acronym = models.CharField(max_length=255,  null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    phone = models.CharField(max_length=255,  null=True, blank=True)
    email = models.EmailField(max_length=255,  null=True, blank=True)
    website = models.URLField(max_length=255,  null=True, blank=True)
    whatsapp = models.CharField(max_length=255,  null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    chef = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='chef_orgao')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/orgaos/%i/" % (self.pk)

    def get_cep(self):
        if self.address:    
            key = os.environ.get('GOOGLEMAPSKEY')
            api_conect = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json?address=" + self.address + "&key=" + key)
            api_conect = api_conect.json()
            address_compontent_size = len(
                api_conect['results'][0]['address_components'])
            return api_conect['results'][0]['address_components'][address_compontent_size-1]['long_name']
            
    def get_latitude(self):
        if self.address:
            key = os.environ.get('GOOGLEMAPSKEY')
            api_conect = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json?address=" + self.address + "&key=" + key)
            api_conect = api_conect.json()
            return api_conect['results'][0]['geometry']['location']['lat']
            
    def get_longitude(self):
        if self.address:
            key = os.environ.get('GOOGLEMAPSKEY')
            api_conect = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json?address=" + self.address + "&key=" + key)
            api_conect = api_conect.json()
            return api_conect['results'][0]['geometry']['location']['lng']
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        if self.address:
            self.latitude = self.get_latitude()
            self.longitude = self.get_longitude()
            self.cep = self.get_cep()
        super(Organ, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Orgão'
        verbose_name_plural = 'Orgãos'
        db_table = 'orgao'
        