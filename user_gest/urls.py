from django.urls import path
from .views import *


urlpatterns = [
    
    path('utilisateur/',UtilisateurListCreate.as_view(),name='utilisateur'),
    path('utilisateur/<int:pk>/',UtilisateurRetrieveUpdateDestroy.as_view(),name='utilisateur'),
]
