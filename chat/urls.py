from django.urls import path 

from .views import * 

urlpatterns = [ 
    path('chat/', HomePage, name='home'),
    path('', Home, name='acc'),
 ]