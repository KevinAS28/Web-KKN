from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question

class ACardPluginModel(models.Model):
    title = models.CharField(max_length=100)
    # text = models.TextField()
    # image = models.ImageField(upload_to='images/')   

class ACardPlugin(CMSPlugin):
    # title = models.ForeignKey(PollPluginModel, on_delete=models.CASCADE)
    title1 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)   