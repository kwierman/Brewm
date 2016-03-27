from __future__ import unicode_literals

from django.db import models

class Brewer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
