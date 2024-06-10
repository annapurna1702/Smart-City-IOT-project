from django.db import models

# Create your models here.



class Credentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    user_status = models.CharField(max_length=100)



class Municiplality(models.Model):
    municipality = models.CharField(max_length=200)
    mayor = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='municipality')
    username = models.CharField(max_length=100)


class WasteBin(models.Model):
    bin_ID = models.AutoField(primary_key=True)
    identity = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='wastebin')
    location = models.CharField(max_length=250)
    landmark = models.CharField(max_length=200)
    agent = models.IntegerField()
    municipality = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    

class Collection_Agent(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to='collection_agent')
    vehicle_number = models.CharField(max_length=100)
    vehicle_image = models.ImageField(upload_to='collection_vehicle')
    username = models.CharField(max_length=100)
    user_status = models.CharField(max_length=100,default="active")
    municipality = models.CharField(max_length=100)
    