from django.db import models


# Create your models here.
class Materia(models.Model):
        nome = models.CharField(max_length=255, unique=True)

        def __str__(self):
            return f'{self.nome} - {self.id}'

class Descricao(models.Model):
        nome = models.CharField(max_length=255, unique=True)
        
        def __str__(self):
            return f'{self.nome} - {self.id}'


class Avaliacao(models.Model):
    descricao = models.ForeignKey(Descricao, on_delete=models.SET_NULL, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
    data = models.DateField(auto_now_add=True, null=True)
    acertos = models.IntegerField()
    erros = models.IntegerField()

    class Meta:
        ordering = ['-data']