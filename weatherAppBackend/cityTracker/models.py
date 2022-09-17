from django.db import models


class City(models.Model):
    """model for city"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
