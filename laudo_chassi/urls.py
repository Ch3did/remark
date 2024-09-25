from django.urls import path

from . import views

urlpatterns = [    
    path('<int:laudo_id>', views.laudo_chassi, name='laudo_chassi'),  
]