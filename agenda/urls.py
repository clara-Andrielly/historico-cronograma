from django.urls import path
from agenda.views import listar_avaliacoes, new_avaliacao

urlpatterns = [
    path("", listar_avaliacoes, name='index'),
    path("new/", new_avaliacao, name='new_avaliacao')
]