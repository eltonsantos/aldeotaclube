# Generated by Django 2.0.4 on 2018-04-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adversario', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('local', models.CharField(max_length=50)),
                ('arbitragem', models.CharField(max_length=80)),
                ('escudo_adversario', models.ImageField(blank=True, null=True, upload_to='jogos')),
            ],
        ),
    ]
