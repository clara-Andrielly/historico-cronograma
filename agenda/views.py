from django.shortcuts import render
from agenda.models import Avaliacao

# Create your views here.
def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.filter().order_by('data')
    return render(
        request=request,
        template_name="agenda/listar_avaliacoes.html", 
        context={'avaliacoes': avaliacoes})