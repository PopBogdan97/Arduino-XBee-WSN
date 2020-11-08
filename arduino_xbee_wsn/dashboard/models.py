from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensor_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.FloatField()
