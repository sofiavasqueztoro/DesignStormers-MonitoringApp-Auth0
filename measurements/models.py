from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    codigo = models.FloatField(null=True, blank=True, default=None)
    producto = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField(default=1)
    estado = models.CharField(max_length=30, choices=[ ('pendiente', 'Pendiente'),('aprobado', 'Aprobado'),('rechazado', 'Rechazado')],default='pendiente')

    def __str__(self):
        return '%s %s %s %s' % (self.codigo, self.producto, self.cantidad, self.estado)