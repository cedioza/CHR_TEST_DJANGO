from django.db import models

class DatosConcesion(models.Model):
    concesion = models.CharField(max_length=100)
    tipo_concesion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    rs_ds = models.CharField(max_length=100)
    tipo_tramite = models.CharField(max_length=100)
    concesionario = models.CharField(max_length=100)
    tipo_vigencia = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.concesion} - {self.tipo_concesion}'