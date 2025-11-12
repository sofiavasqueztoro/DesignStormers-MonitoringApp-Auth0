from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all()
    return (queryset)

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()