from django.urls import path
from .views import *

urlpatterns = [
    path('pregnancy/', afficher_calendrier, name='pregnancy'),
    path('',principal , name='principal'),
    path('poids',compteur , name='compte'),

]
