from django.urls import path

from . import views

urlpatterns = [
    path("<int:laudo_id>", views.laudo_vidros, name="laudo_vidros"),
]
