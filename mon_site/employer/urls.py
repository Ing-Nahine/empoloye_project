

from django.contrib import admin
from django.urls import path

from .views import  liste_employer, ajouter_employer, modifier_employer,suprimer_employer

urlpatterns = [
    
    path('',liste_employer, name='liste_employer'),
    path('ajouter/',ajouter_employer, name='ajouter_employer'),
    path('modifier/<int:id>/',modifier_employer, name='modifier_employer'),
    path('suprimer/<int:id>/',suprimer_employer, name='suprimer_employer'),

    
    
]
