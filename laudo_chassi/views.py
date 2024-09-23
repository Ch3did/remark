from django.shortcuts import render, get_object_or_404
from .models import LaudoChassi

# Create your views here.
def laudo_chassi(request, laudo_id):
    # print(get_config('ultimo_registro'))
    laudo = get_object_or_404(LaudoChassi, pk=laudo_id)        
    context = {
        'laudo': laudo,        
    }
    return render(request, 'laudo_chassi/laudo_chassi.html', context)
