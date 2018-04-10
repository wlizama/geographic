from django.db import models

# Create your models here.
class Country(models.Model):
  CODE_CHOICES = (
    ( 'perú', 'PE' ),
    ( 'colombia', 'CO' ),
    ( 'mexico', 'MX' ),
    ( 'estados unidos', 'USA' ),
    ( 'argentina', 'AR' ),
  )

  name = models.CharField(max_length=255)    
  code = models.CharField(max_length=3, choices=CODE_CHOICES)
