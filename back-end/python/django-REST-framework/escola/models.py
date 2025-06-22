from django.db import models

class Estudantes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):

    OPTIONS_NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.TextField(blank=False)
    nivel = models.CharField(max_length=1,blank=False, null=False, default='B', choices=OPTIONS_NIVEL)

    def __str__(self):
        return self.codigo