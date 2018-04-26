from django import forms
from apps.groups.models import GrupoAlumnos,Grupo,Resultados

class GrupoAlumnosForm(forms.ModelForm):
    class Meta:
        model = GrupoAlumnos
        fields=['Grupo',]
        exclude = ['Usuario']
        labels={
        'Grupo':'Grupo',
        }
        widgets={
        'Grupo':forms.Select(attrs={'class':'form-control'}),
        }

class ResultadosForm(forms.ModelForm):
    class Meta:
        model = Resultados
        exclude =['juego',
        'instrucciones',
        'tiempo',
        'fecha',]
