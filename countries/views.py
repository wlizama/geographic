from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from countries.models import Country

class HomeView(TemplateView):
  template_name = 'countries/home.html'

class CountriesDetailIDView(TemplateView):
  template_name = 'countries/country_id_detail.html'

  def get_context_data(self, *args, **kwargs):
    return {
      "id" : kwargs["id"]
    }

class CountriesDetailView(TemplateView):
  template_name = 'countries/country_detail.html'

  def get_context_data(self, *args, **kwargs):
    return {
      "code" : kwargs["code"]
    }

class CountrySearchView(ListView):
  template_name = "countries/search.html" 
  model = Country

  def get_queryset(self):
    query = self.kwargs["query"]
    return Country.objects.filter(name__contains=query)