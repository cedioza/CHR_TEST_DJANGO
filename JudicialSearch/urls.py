from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='index'),
    path('search',views.guardar_jurisprudencias, name='guardar_jurisprudencias'),
     path('jurisprudencia/', views.tabla_jurisprudencia, name='tabla_jurisprudencia'),
]
