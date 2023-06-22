from django.db import models

# Create your models here.
from django.db import models

class Jurisprudencia(models.Model):
    id = models.IntegerField(primary_key=True)
    tipoCausa = models.CharField(max_length=1)
    rol = models.CharField(max_length=20)
    caratula = models.CharField(max_length=1500)
    nombreProyecto = models.CharField(max_length=1500)
    fechaSentencia = models.DateField()
    descriptores = models.CharField(max_length=1500)
    linkSentencia = models.CharField(max_length=1500)
    urlSentencia = models.CharField(max_length=1500)
    activo = models.BooleanField()
    tribunal = models.CharField(max_length=10)
    tipo = models.CharField(max_length=15)
    relacionada = models.CharField(max_length=1500)
    visitas = models.IntegerField()

    def __str__(self):
        return self.rol

class Valor(models.Model):
    id = models.IntegerField(primary_key=True)
    idParametro = models.IntegerField()
    idItemlista = models.IntegerField(null=True, blank=True)
    valor = models.CharField(max_length=1500, null=True, blank=True)
    parametro = models.CharField(max_length=1500)
    item = models.CharField(max_length=1500)

    jurisprudencia = models.ForeignKey(Jurisprudencia, related_name='valores', on_delete=models.CASCADE)

    def __str__(self):
        return self.parametro