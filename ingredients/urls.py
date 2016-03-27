from django.conf.urls import url
from . import views

app_name="ingredients"

urlpatterns = [
    url(r'^grains/$', views.GrainListView.as_view(), name='grains'),
    url(r'^grains/(?P<pk>[-\w]+)/$', views.GrainDetailView.as_view(), name='grain-detail'),

    url(r'^hops/$', views.HopListView.as_view(), name='hops'),
    url(r'^hops/(?P<pk>[-\w]+)/$', views.HopDetailView.as_view(), name='hop-detail'),

    url(r'^water/$', views.WaterListView.as_view(), name='water'),
    url(r'^water/(?P<pk>[-\w]+)/$', views.WaterDetailView.as_view(), name='water-detail'),

    url(r'^yeasts/$', views.YeastListView.as_view(), name='yeasts'),
    url(r'^yeasts/(?P<pk>[-\w]+)/$', views.YeastDetailView.as_view(), name='yeast-detail'),

    url(r'^data/model$',views.describe_obect, name="describe_obect"),
    url(r'^data/json$',views.data_as_json, name="data_as_json"),
]
