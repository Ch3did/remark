from django.urls import path

from . import views

urlpatterns = [
    path("<int:laudo_id>", views.laudo_etiqueta, name="laudo_etiqueta"),
]
