from django.contrib import admin
from .models import LaudoChassi
from django.contrib.auth.models import Group
# Register your models here.

class LaudoChassiAdmin(admin.ModelAdmin): 
  search_fields = ('placa',)
  list_display = ('modelo', 'ano_veiculo', 'placa')
  change_form_template = 'laudo_chassi/laudo_chassi_change_form.html'  

admin.site.site_header ="REMARK"
admin.site.register(LaudoChassi, LaudoChassiAdmin)