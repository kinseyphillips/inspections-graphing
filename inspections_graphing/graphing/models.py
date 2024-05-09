from django.db import models

class Features_Graph(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    count = models.FloatField()