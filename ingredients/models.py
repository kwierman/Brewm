from __future__ import unicode_literals

from django.db import models


class BaseIngredient(models.Model):
	modification_date = models.DateField(auto_now=True)
	notes = models.CharField(max_length=1000)
	name = models.CharField(max_length=200)
	origin = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Grain(BaseIngredient):
	supplier = models.CharField(max_length=200)
	grain_type = models.IntegerField()
	color = models.DecimalField(decimal_places=2, max_digits=6)
	grain_yield = models.DecimalField(decimal_places=2, max_digits=6)
	coarse_fine_diff = models.DecimalField(decimal_places=2, max_digits=6)
	moisture = models.DecimalField(decimal_places=2, max_digits=6)
	diastatic_power = models.DecimalField(decimal_places=2, max_digits=6)
	protein = models.DecimalField(decimal_places=2, max_digits=6)
	ibu_gal_per_lb = models.DecimalField(decimal_places=2, max_digits=6)


class Hop(BaseIngredient):
	alpha = models.DecimalField(decimal_places=2, max_digits=6)
	beta = models.DecimalField(decimal_places=2, max_digits=6)
	hsi = models.DecimalField(decimal_places=2, max_digits=6)


class Yeast(BaseIngredient):
	product_id = models.CharField(max_length=20)
	attenuation_low = models.DecimalField(decimal_places=2, max_digits=6)
	attenuation_high = models.DecimalField(decimal_places=2, max_digits=6)
	flocculation = models.IntegerField()
	temperature_low = models.DecimalField(decimal_places=2, max_digits=6)
	temperature_high = models.DecimalField(decimal_places=2, max_digits=6)
	best_for = models.CharField(max_length=200)


class Water(BaseIngredient):
	pH = models.DecimalField(decimal_places=2, max_digits=6)
	calcium = models.DecimalField(decimal_places=2, max_digits=6)
	magnesium = models.DecimalField(decimal_places=2, max_digits=6)
	sodium = models.DecimalField(decimal_places=2, max_digits=6)
	sulfate = models.DecimalField(decimal_places=2, max_digits=6)
	chloride = models.DecimalField(decimal_places=2, max_digits=6)
	bicarbonate = models.DecimalField(decimal_places=2, max_digits=6)
	gypsum = models.DecimalField(decimal_places=2, max_digits=6)
	salt = models.DecimalField(decimal_places=2, max_digits=6)
	epsom = models.DecimalField(decimal_places=2, max_digits=6)
	cacl = models.DecimalField(decimal_places=2, max_digits=6)
	soda = models.DecimalField(decimal_places=2, max_digits=6)
	chalk = models.DecimalField(decimal_places=2, max_digits=6)
