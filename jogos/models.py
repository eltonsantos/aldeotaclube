from django.db import models

class Jogos(models.Model):
    adversario = models.CharField(max_length=50)
    data = models.DateField()
    local = models.CharField(max_length=50)
    arbitragem = models.CharField(max_length=80)
    escudo_adversario = models.ImageField(upload_to='jogos', null=True, blank=True)

    def __str__(self):
        return self.adversario
