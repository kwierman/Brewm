from django.contrib import admin

from .models import Grain, Hop, Water, Yeast
# Register your models here.
admin.site.register(Grain)
admin.site.register(Hop)
admin.site.register(Water)
admin.site.register(Yeast)
