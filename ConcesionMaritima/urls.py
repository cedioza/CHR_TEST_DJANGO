from django.urls import path
from . import views

urlpatterns = [
    path('bot',views.bot, name='index'),
    # path('list',views.guardar_jurisprudencias, name='guardar_jurisprudencias'),

]
