from django.db import models
from django.db.models import DO_NOTHING
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=DO_NOTHING)
    listado = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='pictures/%y/%m/%d')

    def __str__(self):
        return self.nome
