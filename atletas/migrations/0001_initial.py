# Generated by Django 2.0.4 on 2018-04-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atletas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('data_nascimento', models.DateField()),
                ('local_nascimento', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='atletas')),
            ],
        ),
    ]