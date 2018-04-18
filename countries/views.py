from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from countries.models import Country
from countries.forms import CountryCreateFormModel

class HomeView(TemplateView):
  template_name = 'countries/home.html'

class CountriesDetailIDView(DetailView):
  template_name = 'countries/country_id_detail.html'
  model = Country

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

class CreateCountryView(TemplateView):
  template_name = "countries/register.html"

  def dispatch(self, request, *args, **kwargs):
    self.form = CountryCreateFormModel(request.POST or None)
    return super().dispatch(request, *args, **kwargs)

  def get_context_data(self, *args, **kwargs):
    return { "form": self.form }

  def post(self, request, *args, **kwargs):
    form = CountryCreateFormModel(request.POST)

    if self.form.is_valid():
      country = form.save()
      return JsonResponse({ "name" : country.name })

    return self.get(request, *args, **kwargs)