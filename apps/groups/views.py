from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.utils.timezone import localtime, now
from apps.groups.forms import *
from apps.groups.models import *
from apps.alumnos.forms import ResultadosForm
from django.contrib.auth.models import User
from apps.groups.models import GrupoAlumnos
from django.contrib import messages
@login_required(login_url='/login/')
def vista_Grupos(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.Usuario = request.user
            grupo.save()
            id_grupo = str(Grupo.objects.last())
            messages.success(request,"Tu grupo tiene el id " + id_grupo)
            return redirect('maestrosIndex')
    else:
        form = GrupoForm()
    context = {"form":form}
    return render(request,'grupos/crearGrupo.html',context)
@login_required(login_url='/login/')
def lista_grupos(request):
    grupos = Grupo.objects.all()
    context = {'grupos':grupos}
    return render(request,'grupos/listaGrupos.html',context)

@login_required(login_url='/login/')
def vista_lista_juegos(request,id_grupo):
    grupo=Grupo.objects.get(id=id_grupo)
    juegos = Juego.objects.filter(grupo=grupo)
    context = {'juegos':juegos}
    return render(request,'grupos/listaJuegos.html',context)

@login_required(login_url='/login/')
def vista_lista_GrupodeAlumnos(request,id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    grupoDeAlumnos = GrupoAlumnos.objects.filter(Grupo=grupo)
    context = {'grupoDeAlumnos':grupoDeAlumnos}
    return render(request,'grupos/listaGrupoAlumnos.html',context)

@login_required(login_url='/login/')
def vista_juego_agregar(request, id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    if request.method== 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            juego = form.save(commit=False)
            juego.grupo = grupo
            juego.save()
            messages.success(request,"Juego creado con éxito")
            return redirect('listaGrupos')
    else:
        form = JuegoForm()
    context ={'form':form}
    return render(request,'grupos/nuevoJuego.html',context)

@login_required(login_url='/login/')
def visa_juego_eliminar(request,id_juego):
    juego = Juego.objects.get(id=id_juego)
    if juego:
        juego.delete()
        messages.success(request,"Juego eliminado con éxito")
    else:
        messages.success(request,"No se pudo eliminar el juego")
    return redirect('listaGrupos')

@login_required(login_url='/login/')
def vista_resultadosAlumnos(request,cadena):
    vector = cadena.split(",")
    form = ResultadosForm();
    resultados = form.save(commit=False);
    juego = Juego.objects.get(id=vector[0])
    resultados.usuario = request.user
    resultados.juego = juego
    resultados.tiempo = vector[1]
    resultados.instrucciones = vector[2]
    resultados.fecha= localtime(now())
    resultados.save();
    messages.success(request,"Felicidades, tu respuesta fue correcta")
    context = {'resultados':resultados}
    return render(request,'Alumnos/resultadosAlumnos.html',context)

def vista_listaResultadosAlumnos(request,id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    resultados = Resultados.objects.filter(usuario=request.user)
    context ={'resultados':resultados}
    return render(request,'Alumnos/listaResultadosAlumnos.html',context)
