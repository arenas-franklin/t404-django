# Generated by Django 2.2.3 on 2019-07-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True, verbose_name='Nome de ideia')),
                ('descricao', models.TextField(verbose_name='Descreva sua ideia')),
                ('categorias', models.CharField(choices=[('TERRA_PLANA', 'Terra Plana'), ('CONTRA_GROGER', 'Ideias para Coach Groger'), ('CONTRA_JOAO', 'Ideias contra João'), ('PUBLICAS', 'Publicas'), ('OUTROS', 'Outroa')], max_length=255, verbose_name='Categorias')),
                ('categoria_outros', models.CharField(blank=True, max_length=255, null=True, verbose_name='Caso outros, qual?')),
                ('data_de_criacai', models.DateTimeField(auto_now_add=True)),
                ('data_de_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('pessoa', models.ForeignKey(on_delete=None, to='website.Pessoa')),
            ],
        ),
    ]
