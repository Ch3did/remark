from django.contrib import admin
from django.contrib.auth.models import Group

from .models import LaudoVidros

# Register your models here.


class LaudoVidrosAdmin(admin.ModelAdmin):
    search_fields = ("placa",)
    list_display = ("modelo", "ano_veiculo", "placa")
    change_form_template = "laudo_vidros/laudo_vidros_change_form.html"


admin.site.site_header = "REMARK"
admin.site.site_url = None
admin.site.dashboard = []
admin.site.index_template = "admin/index.html"
admin.site.index_title = "Selecione um Tipo de Laudo:"
admin.site.base_site = "admin/base_site.html"

admin.site.register(LaudoVidros, LaudoVidrosAdmin)
