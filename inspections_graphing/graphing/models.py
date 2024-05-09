from django.db import models

class Graph(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)
    count = models.FloatField()