from django.shortcuts import render
from django.views.generic import TemplateView

class ContinentsView(TemplateView):
  template_name = 'continents/continents.html'

  def get_context_data(self, *args, **kwargs):
    return {
      "continents" : [
          { "name": "america", "color": "#E3BF1D"},
          { "name": "asia", "color": "#289F31"},
          { "name": "europa", "color": "#D25732"},
          { "name": "oceania", "color": "#335485"}
        ]
    }