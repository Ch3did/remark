from django.contrib import admin
from .models import LaudoPlaqueta
from django.contrib.auth.models import Group
# Register your models here.

class LaudoPlaquetaAdmin(admin.ModelAdmin): 
  search_fields = ('placa',)
  list_display = ('modelo', 'ano_veiculo', 'placa')
  change_form_template = 'laudo_plaqueta/laudo_plaqueta_change_form.html'  

admin.site.site_header ="REMARK"
admin.site.register(LaudoPlaqueta, LaudoPlaquetaAdmin)