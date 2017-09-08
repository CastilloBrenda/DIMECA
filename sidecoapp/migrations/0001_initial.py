# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desempleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_trabajo', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.IntegerField()),
                ('razon_social', models.CharField(max_length=50)),
                ('rubro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OfertaLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajo_solicitado', models.CharField(max_length=50)),
                ('empresa_oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidecoapp.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='oferta_laboral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidecoapp.OfertaLaboral'),
        ),
    ]
