# Generated by Django 2.0.4 on 2018-05-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(blank=True, default='default.png', null=True, upload_to='noticias')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
            },
        ),
    ]
