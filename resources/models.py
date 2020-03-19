from django.db import models

class Disco(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)
    discos = models.ManyToManyField(Disco)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']