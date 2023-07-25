from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll
from datetime import date

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question

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