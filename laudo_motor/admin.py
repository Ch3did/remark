from django.contrib import admin
from .models import LaudoMotor
from django.contrib.auth.models import Group
# Register your models here.

class LaudoMotorAdmin(admin.ModelAdmin): 
  search_fields = ('placa',)
  list_display = ('modelo', 'ano_veiculo', 'placa')
  change_form_template = 'laudo_motor/laudo_motor_change_form.html'  

admin.site.site_header ="REMARK"
admin.site.register(LaudoMotor, LaudoMotorAdmin)