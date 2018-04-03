from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

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