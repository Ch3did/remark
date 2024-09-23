from django.shortcuts import get_object_or_404, render

from .models import LaudoMotor


# Create your views here.
def laudo_motor(request, laudo_id):
    # print(get_config('ultimo_registro'))
    laudo = get_object_or_404(LaudoMotor, pk=laudo_id)
    context = {
        "laudo": laudo,
    }
    return render(request, "laudo_motor/laudo_motor.html", context)
