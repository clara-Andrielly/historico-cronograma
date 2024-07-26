from django.shortcuts import render
from agenda.models import Avaliacao
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from agenda.models import Avaliacao
from django.utils.text import slugify

# Create your views here.
class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['descricao', 'materia', 'acertos', 'erros']


def new_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            new_avaliacao = form.save(commit=False)
            new_avaliacao.slug = slugify(new_avaliacao.descricao)
            new_avaliacao.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AvaliacaoForm()
    return render(request, "new_avaliacao.html", {'form': form})

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.filter().order_by('data')
    return render(
        request=request,
        template_name='index.html', 
        context={'avaliacoes': avaliacoes})