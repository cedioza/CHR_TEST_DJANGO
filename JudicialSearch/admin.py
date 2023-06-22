from django.contrib import admin
from .models import Jurisprudencia

@admin.register(Jurisprudencia)
class JurisprudenciaAdmin(admin.ModelAdmin):
    list_display = ('rol', 'tipoCausa', 'tribunal', 'fechaSentencia')  # Campos a mostrar en la lista
    list_filter = ('tipoCausa', 'tribunal')  # Campos para filtrar
    search_fields = ('rol', 'caratula', 'nombreProyecto')  # Campos para buscar
