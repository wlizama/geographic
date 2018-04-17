from django.shortcuts import render
from django.http import JsonResponse
from people.forms import RegisterForm

def register(request):
  form = RegisterForm(request.POST or None)

  if form.is_valid():
    return JsonResponse(form.cleaned_data)

  return render(request, "people/register.html", { "form" : form })

