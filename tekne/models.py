from django.db import models

# Create your models here.

class ucret(models.Model):
    ucretid = models.AutoField(primary_key=True)
    ucret= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ucret
    
class tur(models.Model):
    turid = models.AutoField(primary_key=True)
    turname= models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.tur
    
class tekne(models.Model):
    tekneid = models.AutoField(primary_key=True)
    teknename= models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.tekne
    
class rezerve(models.Model):
    id = models.AutoField(primary_key=True)
    tarih = models.DateField(blank=True,null=True)
    turname= models.CharField(max_length=50,blank=True, null=True)
    teknename= models.CharField(max_length=50,blank=True, null=True)
    adet= models.IntegerField(blank=True, null=True)
    ucret= models.IntegerField(blank=True, null=True)
    toplamucret= models.IntegerField(blank=True, null=True )
    kapora= models.CharField(max_length=50,blank=True, null=True)
    telno= models.CharField(max_length=50,blank=True, null=True)
    aciklama= models.CharField(max_length=250,blank=True, null=True)
    tamucret = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.rezerve
