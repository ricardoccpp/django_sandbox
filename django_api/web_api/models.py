from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'