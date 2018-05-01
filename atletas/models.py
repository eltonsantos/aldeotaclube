from django.db import models

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    local_nascimento = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='atletas', null=True, blank=True)

    def __str__(self):
        return self.nome + " " + self.sobrenome