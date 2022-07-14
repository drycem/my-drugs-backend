from pyexpat import model
from statistics import mode
from django.db import models

class Drug(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=250)
    code = models.TextField(max_length=250, unique=True)
    atc = models.TextField(max_length=250)
    etken = models.TextField(max_length=250, blank=True, null=True)
    firma = models.TextField(max_length=250, blank=True, null=True)
    durum = models.TextField(max_length=250, blank=True, null=True)


class SgkDrug(models.Model):
    ID = models.IntegerField(primary_key=True)
    BARKOD = models.TextField(max_length=250, unique=True)
    ILAC_ADI = models.TextField(max_length=250)
    SGK_ILAC_KODU = models.TextField(max_length=250)
    AMBALAJ_MIKTARI = models.FloatField()
    TEK_DOZ_MIKTARI = models.FloatField()
    DURUM = models.TextField(max_length=250)
    AKTIF = models.BooleanField()
