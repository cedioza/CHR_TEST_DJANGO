from django.shortcuts import render, redirect
from .models import Valor,Jurisprudencia
import json

import datetime

from django.shortcuts import render, redirect

from .forms import DynamicForm
from .Helpers import helpers
import re

def dashboard(request):
    fields_data = [
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/tribunales",
            'label': "Tribunal"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/years",
            'label': "Año"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/tipo-causas",
            'label': "causas"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/doctrinas/revistas",
            'label': "revistas"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/competencias",
            'label': "competencias"
        },        
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/materias",
            'label': "materias"
        },   
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/componentes-ambientales",
            'label': "componentes"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/tipo-de-recursos",
            'label': "tipo-de-recursos"
        },
        {
            'url': "https://www.buscadorambiental.cl/buscador-api/parametros/jurisprudencias/ministros-redactores",
            'label': "ministros-redactores"
        },
         
        # Agrega más URLs y etiquetas aquí
    ]

    forms = []

    for field_data in fields_data:
        url = field_data['url']
        label = field_data['label']

        dynamic_choices = helpers.get_page_data(url)  # Obtener las opciones dinámicas desde la URL

    
        form = DynamicForm(dynamic_choices=dynamic_choices, label=label)

        forms.append(form)

           

    return render(request, 'index.html', {'forms': forms})



def guardar_jurisprudencias(request):


    data = helpers.get_data_search()
    # Reemplazar espacios por "%20" en la clave "urlSentencia" de cada elemento
    data = data.json()

    jurisprudencias = data["jurisprudencias"]

    for element in jurisprudencias:
        urlSentencia = element.get("urlSentencia")
        if urlSentencia:
            element["urlSentencia"] = re.sub(r"\s", "%20", urlSentencia)

        valores = element.get("valores")
        if valores:
            for item in valores:
                valor = item.get("valor")
                if valor and isinstance(valor, str) and "https" in valor:
                    item["valor"] = re.sub(r"\s", "%20", valor)

    data["jurisprudencias"] = jurisprudencias

    for jurisprudencia_data in data['jurisprudencias']:
        # Crea una instancia de Jurisprudencia
        jurisprudencia = Jurisprudencia()

        # Establece los valores de los campos
        jurisprudencia.id = jurisprudencia_data['id']
        jurisprudencia.tipoCausa = jurisprudencia_data['tipoCausa']
        jurisprudencia.rol = jurisprudencia_data['rol']
        jurisprudencia.caratula = jurisprudencia_data['caratula']
        jurisprudencia.nombreProyecto = jurisprudencia_data['nombreProyecto']
        jurisprudencia.fechaSentencia = datetime.datetime.strptime(jurisprudencia_data['fechaSentencia'], "%d-%m-%Y").date()
        jurisprudencia.descriptores = jurisprudencia_data['descriptores']
        jurisprudencia.linkSentencia = jurisprudencia_data['linkSentencia']
        jurisprudencia.urlSentencia = jurisprudencia_data['urlSentencia']
        jurisprudencia.activo = jurisprudencia_data['activo']
        jurisprudencia.tribunal = jurisprudencia_data['tribunal']
        jurisprudencia.tipo = jurisprudencia_data['tipo']
        jurisprudencia.relacionada = jurisprudencia_data['relacionada']
        jurisprudencia.visitas = jurisprudencia_data['visitas']

        # Guarda la instancia de Jurisprudencia
        jurisprudencia.save()

        for valor_data in jurisprudencia_data['valores']:
            # Crea una instancia de Valor
            valor = Valor()

            # Establece los valores de los campos
            valor.id = valor_data['id']
            valor.idParametro = valor_data['idParametro']
            valor.idItemlista = valor_data['idItemlista']
            valor.valor = valor_data['valor']
            valor.parametro = valor_data['parametro']
            item = valor_data['item']
            valor.item = 'No information' if item is None else item

            # Establece la relación con la instancia de Jurisprudencia
            valor.jurisprudencia = jurisprudencia

            # Guarda la instancia de Valor

            valor.save()


    return redirect(' ')


def tabla_jurisprudencia(request):
    jurisprudencias = Jurisprudencia.objects.all()
    return render(request, 'tabla_jurisprudencia.html', {'jurisprudencias': jurisprudencias})