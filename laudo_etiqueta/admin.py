from django.contrib import admin
from django.contrib.auth.models import Group

from .models import LaudoEtiqueta

# Register your models here.


class LaudoEtiquetaAdmin(admin.ModelAdmin):
    search_fields = ("placa",)
    list_display = ("modelo", "ano_veiculo", "placa")
    change_form_template = "laudo_etiqueta/laudo_etiqueta_change_form.html"


admin.site.site_header = "REMARK"
admin.site.register(LaudoEtiqueta, LaudoEtiquetaAdmin)
