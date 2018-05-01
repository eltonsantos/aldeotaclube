from django.db import models

class Jogo(models.Model):
    adversario = models.CharField(max_length=50)
    data = models.DateField()
    local = models.CharField(max_length=50)
    arbitragem = models.CharField(max_length=80, null=True, blank=True)
    escudo_adversario = models.ImageField(default="sem_escudo.png", upload_to='jogos', null=True, blank=True)
    placar_aldeota = models.IntegerField(null=True, blank=True)
    placar_adversario = models.IntegerField(null=True, blank=True)
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.adversario

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"
