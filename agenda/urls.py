from django.urls import path
from agenda.views import listar_avaliacoes

urlpatterns = [
    path("", listar_avaliacoes, name='listar_avaliacoes'),
]