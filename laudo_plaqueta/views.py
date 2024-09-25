from django.shortcuts import render, get_object_or_404
from .models import LaudoPlaqueta

# Create your views here.
def laudo_plaqueta(request, laudo_id):
    # print(get_config('ultimo_registro'))
    laudo = get_object_or_404(LaudoPlaqueta, pk=laudo_id)        
    context = {
        'laudo': laudo,        
    }
    return render(request, 'laudo_plaqueta/laudo_plaqueta.html', context)
