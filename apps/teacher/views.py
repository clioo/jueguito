from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.groups.models import *
from apps.alumnos.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request,id_grupo, format=None):
        data = {
        "usuarios": 100,
        "resultados": 200,
        }
        return Response(data)


@login_required(login_url='/login/')
def MaestrosIndex(request):
    tipo = str(request.user.profile.tipo)
    if tipo=='A':
        return redirect('alumnosIndex')
    else:
        return render(request,'maestros/maestrosIndex.html')

def vista_listaResultadosGrupos(request,id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    usuarios = GrupoAlumnos.objects.filter(Grupo=grupo)
    resultados = Resultados.objects.all()
    context ={'resultados':resultados,
                    'usuarios':usuarios,
                    'grupo':grupo}
    return render(request,'maestros/listaResultadosGrupos.html',context)
# Create your views here.
def vista_graficasMaestros(request,id_grupo):
    user = []
    results = []
    grupo = Grupo.objects.get(id=id_grupo)
    usuarios = GrupoAlumnos.objects.filter(Grupo=grupo)
    for usuario in usuarios:
        user.append(usuario.Usuario.username)
        juegos = Juego.objects.filter(grupo=grupo)
        print(Resultados.objects.filter(usuario=usuario.Usuario).count())
        results.append(Resultados.objects.filter(usuario=usuario.Usuario).count())

    titulo = "Actividad de alumnos"
    context = {
    'id_grupo':id_grupo,
    'user':user,
    'results':results,
    'titulo':titulo,
    }
    return render(request,'maestros/graficasMaestros.html',context)
    pass
