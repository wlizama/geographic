from django.db import models

# Create your models here.

class Continent(models.Model):
  name = models.CharField(max_length=255)
  translate = models.CharField(max_length=255)
  color = models.CharField(max_length=255)

  def __str__(self):
    return self.name