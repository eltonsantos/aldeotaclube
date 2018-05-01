from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    conteudo = models.TextField()
    imagem = models.ImageField(default='default.png', upload_to='noticias', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def snippet(self):
        return self.conteudo[:50] + '...'

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
