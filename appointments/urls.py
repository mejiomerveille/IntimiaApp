from django.urls import path
from appointments import views

urlpatterns = [
    path('', views.home, name='hom'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
]
