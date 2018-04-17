from django.shortcuts import render
from django.http import JsonResponse
from people.forms import RegisterForm

def register(request):
  form = RegisterForm()

  if request.method == "GET":
    return render(request, "people/register.html", { "form" : form })

  return JsonResponse(request.POST)
