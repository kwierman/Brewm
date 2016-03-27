from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Grain, Hop, Water, Yeast, BeerStyle, Brewer

"""
Serves the index page
"""

def index(request):
    context={}
    return render(request, 'brewtables/index.html', context)

"""
    List View
"""

class IngredientListView(ListView):
    paginate_by = 25
    template_name = "brewtables/ingredient_list.html"
    ingredient_name="None"
    ingredient_url="brewtables:grains"
    ingredient_detail_url="brewtables:grain-detail"

    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['fields'] = [i.name for i in self.model._meta.get_fields()]
        context['ingredient_name']=self.ingredient_name
        context['ingredient_url']=self.ingredient_url
        context['ingredient_detail_url']=self.ingredient_detail_url
        return context


class GrainListView(IngredientListView):
    model = Grain
    queryset = model.objects.order_by('name')
    ingredient_name="Grain"
    ingredient_url="brewtables:grains"
    ingredient_detail_url="brewtables:grain-detail"

class HopListView(IngredientListView):
    model = Hop
    queryset = model.objects.order_by('name')
    ingredient_name="Hop"
    ingredient_url="brewtables:hops"
    ingredient_detail_url="brewtables:hop-detail"


class WaterListView(IngredientListView):
    model = Water
    queryset = model.objects.order_by('name')
    ingredient_name="Water"
    ingredient_url="brewtables:water"
    ingredient_detail_url="brewtables:water-detail"


class YeastListView(IngredientListView):
    model = Yeast
    queryset = model.objects.order_by('name')
    ingredient_name="Yeast"
    ingredient_url="brewtables:yeasts"
    ingredient_detail_url="brewtables:yeast-detail"


"""
    Detail Views
"""
class IngredientDetailView(DetailView):
    slug_field = 'name'
    template_name = "brewtables/ingredient_detail.html"
    def get_context_data(self, **kwargs):
        context = super(IngredientDetailView, self).get_context_data(**kwargs)
        context['fields'] = [i.name for i in self.model._meta.get_fields()]
        context['ingredient_name'] = "Placeholder Text"
        return context


class GrainDetailView(IngredientDetailView):
    model = Grain


class HopDetailView(IngredientDetailView):
    model = Hop


class YeastDetailView(IngredientDetailView):
    model = Yeast


class WaterDetailView(IngredientDetailView):
    model = Water
