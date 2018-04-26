from django import forms
from apps.groups.models import Grupo,Juego
class GrupoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model=Grupo
        fields=[
        'descripcion',
        ]
        exclude = ['Usuario']

class JuegoForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=100,label="Descripción",widget=forms.Textarea(attrs={'class':'form-control'}))
    entrada = forms.CharField(label="Valores de entrada",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    salida = forms.CharField(label="Valores de salida",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    piso = forms.CharField(label="Valores del piso",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    class Meta:
        model = Juego
        fields=[
        'descripcion',
        'entrada',
        'salida',
        'piso',

        ]
        exclude = ['Usuario']

class ListaJuegosForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=100,label="Descripción",widget=forms.Textarea(attrs={'class':'form-control'}))
    entrada = forms.CharField(label="Valores de entrada",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    salida = forms.CharField(label="Valores de salida",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    piso = forms.CharField(label="Valores del piso",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Valores separados por coma"}))
    class Meta:
        model = Juego
        fields=[
        'descripcion',
        'entrada',
        'salida',
        'piso',
        ]
        exclude = ['Usuario']
