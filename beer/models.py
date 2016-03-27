from __future__ import unicode_literals

from django.db import models

class BeerStyle(models.Model):
	name= models.CharField(max_length=200)
	category= models.CharField(max_length=200)
	min_og = models.DecimalField(decimal_places=2, max_digits=6)
	max_og = models.DecimalField(decimal_places=2, max_digits=6)
	min_fg = models.DecimalField(decimal_places=2, max_digits=6)
	max_fg = models.DecimalField(decimal_places=2, max_digits=6)
	min_ibu = models.DecimalField(decimal_places=2, max_digits=6)
	max_ibu = models.DecimalField(decimal_places=2, max_digits=6)
	min_carb = models.DecimalField(decimal_places=2, max_digits=6)
	max_carb = models.DecimalField(decimal_places=2, max_digits=6)
	min_color = models.DecimalField(decimal_places=2, max_digits=6)
	max_color = models.DecimalField(decimal_places=2, max_digits=6)
	min_abv = models.DecimalField(decimal_places=2, max_digits=6)
	max_abv = models.DecimalField(decimal_places=2, max_digits=6)
	description = models.CharField(max_length=200)
	profile  = models.CharField(max_length=200)
	ingredients = models.CharField(max_length=200)
	examples = models.CharField(max_length=200)
	web_link = models.URLField()
    
class Beer:
	name = models.CharField(max_length=200)
	brewer = models.CharField(max_length=200)

	def __str__(self):
		return self.name
