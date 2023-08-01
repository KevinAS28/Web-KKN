from django.db import models
from cms.models.fields import PlaceholderField
from cms.plugin_base import CMSPluginBase, CMSPlugin
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _
from datetime import date


class ACardPluginModel(models.Model):
    title = models.CharField(max_length=100)
    # text = models.TextField()
    # image = models.ImageField(upload_to='images/')   
  
class HomeCardImage(models.Model):
    title = models.CharField(max_length=100)
    tanggal = models.DateField(default=date.today)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   

class HomeCardImagePlugin(CMSPlugin):
    # home_card_image = models.ForeignKey(HomeCardImage, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    tanggal = models.DateField(default=date.today)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)       
    link_detail = models.CharField(max_length=1000)

class HomeCardImageWidePlugin(CMSPlugin):
    # home_card_image = models.ForeignKey(HomeCardImage, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)       
    detail = models.CharField(max_length=1000)

class HomeBeritaCardPlugin(CMSPlugin):
    # home_card_image = models.ForeignKey(HomeCardImage, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)       
    detail = models.CharField(max_length=1000)

class PejabatCardPlugin(CMSPlugin):
    # title = models.ForeignKey(PollPluginModel, on_delete=models.CASCADE)
    tingkat_jabatan = models.CharField(max_length=100)
    nama_pejabat = models.CharField(max_length=100)
    tanggal_mulai_menjabat = models.DateField(default=date.today)#models.CharField(max_length=100)
    tanggal_akhir_jabatan = models.DateField(default=date.today)#models.CharField(max_length=5000)
    foto = models.ImageField(upload_to='images/', blank=True, null=True)   

class SmallGalleryPlugin(CMSPlugin):
    # title = models.ForeignKey(PollPluginModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   

class PetaLivePlugin(CMSPlugin):
    link = models.CharField(max_length=500)

class UMKMPlugin(CMSPlugin):
    image = models.ImageField(upload_to='images/', blank=True, null=True)   
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    price = models.IntegerField()    
    link_ecommerce = models.CharField(max_length=1000)
    placeholder_field = PlaceholderField(slotname="placeholder slot name", null=True, blank=True)

class WisataPlugin(CMSPlugin):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    link_location = models.CharField(max_length=1000)

class ProfilGaleriPlugin(CMSPlugin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   
    tanggal = models.DateField(default=date.today)

class ProfilArtikelPlugin(CMSPlugin):
    title = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   
    tanggal = models.DateField(default=date.today)
    link = models.CharField(max_length=500)

class PerangkatDesaPlugin(CMSPlugin):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   

class ImageResponsivePlugin(CMSPlugin):
    image = models.ImageField(upload_to='images/', blank=True, null=True)   