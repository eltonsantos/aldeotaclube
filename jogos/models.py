from django.db import models

class Jogo(models.Model):
    adversario = models.CharField(max_length=50)
    data = models.DateField()
    local = models.CharField(max_length=50)
    arbitragem = models.CharField(max_length=80, null=True, blank=True)
    escudo_adversario = models.ImageField(upload_to='jogos', null=True, blank=True)
    placar_aldeota = models.CharField(max_length=10, null=True, blank=True)
    placar_adversario = models.CharField(max_length=10, null=True, blank=True)
    resumo = models.TextField()

    def __str__(self):
        return self.adversario

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
