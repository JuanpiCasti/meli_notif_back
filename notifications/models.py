from django.db import models

# Create your models here.
class Notification(models.Model):
    resource = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    topic = models.CharField(max_length=20)
    application_id = models.BigIntegerField()
    attempts = models.PositiveIntegerField()
    sent = models.CharField(max_length=100)
    received = models.CharField(max_length=100)