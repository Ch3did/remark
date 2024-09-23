from django.shortcuts import get_object_or_404, render

from .models import LaudoVidros


# Create your views here.
def laudo_vidros(request, laudo_id):
    # print(get_config('ultimo_registro'))
    laudo = get_object_or_404(LaudoVidros, pk=laudo_id)
    context = {
        "laudo": laudo,
    }
    return render(request, "laudo_vidros/laudo_vidros.html", context)
