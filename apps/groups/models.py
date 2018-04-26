from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.

class Grupo(models.Model):
    Usuario =models.ForeignKey(User)
    descripcion = models.CharField(max_length=30)
    def definirCadena(self):
        cadena = "{0}"
        return cadena.format(self.id)
    def __str__(self):
        return self.definirCadena()

class GrupoAlumnos(models.Model):
    Usuario = models.ForeignKey(User)
    Grupo = models.ForeignKey(Grupo)
    class Meta:
        unique_together= ('Usuario','Grupo')
    def definirCadena(self):
        cadena = "{0},{1}"
        return cadena.format(self.Usuario,self.Grupo)
    def __str__(self):
        return self.definirCadena()
class Juego(models.Model):
    grupo = models.ForeignKey(Grupo)
    descripcion = models.TextField(max_length=100)
    entrada = models.TextField(max_length=50,validators=[validate_comma_separated_integer_list])
    salida = models.TextField(max_length=50,validators=[validate_comma_separated_integer_list])
    piso=models.TextField(max_length=50,validators=[validate_comma_separated_integer_list])

class Resultados(models.Model):
    usuario = models.ForeignKey(User)
    juego = models.ForeignKey(Juego)
    tiempo = models.CharField(max_length=12)
    instrucciones = models.IntegerField()
    fecha = models.DateTimeField()

admin.site.register(Grupo)
admin.site.register(GrupoAlumnos)
admin.site.register(Resultados)
