from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias', null=True, blank=True)

    def __str__(self):
        return self.titulo
