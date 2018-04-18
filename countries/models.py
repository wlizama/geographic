from django.db import models

class ActiveManager(models.Manager):
  
  def get_query_set(self):
    return suoper().get_queryset().filter(active=True)


# Create your models here.
class Country(models.Model):
  CODE_CHOICES = (
    ( 'PE' , 'perú'),
    ( 'CO', 'colombia' ),
    ( 'MX', 'mexico' ),
    ( 'USA', 'estados unidos' ),
    ( 'AR', 'argentina' ),
  )

  name = models.CharField(max_length=255)    
  code = models.CharField(max_length=3, choices=CODE_CHOICES)
  continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)
  active = models.BooleanField(default=True)
  active_manager = ActiveManager()
  objects = models.Manager() # conservar el object manager por defecto

  def __str__(self):
    return self.name