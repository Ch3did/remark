from django.shortcuts import render, get_object_or_404
from .models import LaudoEtiqueta

# Create your views here.
def laudo_etiqueta(request, laudo_id):
    # print(get_config('ultimo_registro'))
    laudo = get_object_or_404(LaudoEtiqueta, pk=laudo_id)        
    context = {
        'laudo': laudo,        
    }
    return render(request, 'laudo_etiqueta/laudo_etiqueta.html', context)
