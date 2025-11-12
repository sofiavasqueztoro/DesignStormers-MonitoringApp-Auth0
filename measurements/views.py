from django.shortcuts import render
from .forms import MeasurementForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_measurement import create_measurement, get_measurements
from monitoring.auth0backend import getRole

def measurement_list(request):
    measurements = get_measurements()
    context = {
        'measurement_list': measurements
    }
    return render(request, 'Measurement/pedidos.html', context)

def measurement_create(request):
    role = getRole(request)
    if role == "Coordinador Bodega":
        if request.method == 'POST':
            form = MeasurementForm(request.POST)
            if form.is_valid():
                create_measurement(form)
                messages.add_message(request, messages.SUCCESS, 'Measurement create successful')
                return HttpResponseRedirect(reverse('measurementCreate'))
            else:
                print(form.errors)
        else:
            form = MeasurementForm()

        context = {
            'form': form,
        }

    return render(request, 'Measurement/pedidocreate.html', context)