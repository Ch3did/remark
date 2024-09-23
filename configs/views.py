from django.shortcuts import render, get_object_or_404
from .models import Configs

# Create your views here.
def get_config(_config):
  config = get_object_or_404(Configs, chave=_config)
  return config.valor

def set_config(_config, _new_value):
  config = get_object_or_404(Configs, chave=_config)
  config.valor = _new_value
  config.save()
  print('Salvou')