from django.db import models

# Create your models here.
class Configs(models.Model):
  chave = models.CharField(max_length=30)
  valor = models.CharField(max_length=30)