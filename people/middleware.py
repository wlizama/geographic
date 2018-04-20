from django.http import Http404 
import random

class ABMiddleware:

   def __init__(self, get_response):
       self.get_response = get_response
  
   def __call__(self, request):
       # Antes de ejecutar vista
       if not 'testab' in request.session:
           request.session['testab'] =  random.choice(['a', 'b'])
      
       response = self.get_response(request)
      
       # Después de ejecutar vista
       return response