from django.db import models

# Create your models here.


class WebHook(models.Model):
    webhook_id = models.IntegerField()
    type = models.CharField(max_length=200)
    events = models.CharField(max_length=200)