#coding: utf-8
from django.shortcuts import render,redirect,render_to_response
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.alumnos.forms import GrupoAlumnosForm
from django.db import IntegrityError
from apps.alumnos.forms import ResultadosForm
from apps.groups.models import GrupoAlumnos,Grupo,Juego,Resultados
import jsonpickle
# Create your views here.
@login_required(login_url='/login/')
def alumnosIndex(request):
    tipo =str(request.user.profile.tipo)
    if  tipo=='A':
        return render(request,'Alumnos/alumnosIndex.html')
    else:
        return render(request,'Maestros/maestrosIndex.html')

def vista_graficasAlumnos(request,id_juego):
    user = []
    results = []
    juego = Juego.objects.get(id=id_juego)
    resultados = Resultados.objects.filter(juego=juego)
    if resultados:
        user.append('Tiempo')
        results.append(resultados[0].tiempo)
        user.append('Instrucciones')
        results.append(resultados[0].instrucciones)
        titulo = "Intento mas reciente"
        pass
    else:
        titulo = "No has jugado este juego"
    context = {
        'titulo':titulo,
        'user':user,
        'results':results,
        }
    return render(request,'maestros/graficasMaestros.html',context)
    pass


@login_required(login_url='/login/')
def Index(request):
    return render(request,'index.html')


@login_required(login_url='/login/')
def juego(request, id_grupo,id_juego): #AQUI TAMBIEN IMBECIL
    hayResultados = False;
    form = ResultadosForm()
    grupo = Grupo.objects.get(id=id_grupo)
    juegos = Juego.objects.filter(grupo=grupo)
    if juegos: #checa si hay juegos en ese grupos
        for juego in juegos:
            resultados = Resultados.objects.filter(juego=juego,usuario=request.user)
            if not resultados:
                entradas = juego.entrada.split(",")
                salidas = juego.salida.split(",")
                piso = juego.piso.split(",")
                for i in range(len(piso),6):
                    piso.append("0")
                    pass
                context = {'form':form,
                'entradas':entradas,
                'salidas':salidas,
                'piso':piso,
                'id_grupo':id_grupo,
                'juego':juego,
                }
                print(entradas)
                return render(request,'dragNdrop.html',context=context)
        if (id_juego != '0'):
            juego = Juego.objects.get(id=id_juego)
            entradas = juego.entrada.split(",")
            salidas = juego.salida.split(",")
            piso = juego.piso.split(",")
            for i in range(len(piso),6):
                piso.append("0")
                pass
            context = {'form':form,
            'entradas':entradas,
            'salidas':salidas,
            'piso':piso,
            'id_grupo':id_grupo,
            'juego':juego,
            }
            print(entradas)
            return render(request,'dragNdrop.html',context=context)
            #HASTA AQUI BORRAS WEY
        else:
            messages.success(request,'Ya terminaste todos los juegos! Felicidades, ya no juegues por favor, gracias')
            return redirect('gruposUnidos')
    else:
        messages.success(request,'No hay juegos en este grupo')
        return redirect('gruposUnidos')


    pass


@login_required(login_url='/login/')
def vista_GrupoAlumnos(request):
    if request.method == 'POST':
        form = GrupoAlumnosForm(request.POST)
        try:
            if form.is_valid():
                grupo = form.save(commit=False)
                grupo.Usuario = request.user
                grupo.save()
                messages.success(request,"Felicidades, te has unido al grupo!")
                return redirect('gruposUnidos')
        except IntegrityError as e:
            messages.success(request,'Ya estás en ese grupo')
    else:
        form = GrupoAlumnosForm()
    context = {"form":form}
    return render(request,'Alumnos/unirseGrupo.html',context)

@login_required(login_url='/login/')
def vista_ListaGruposUnidos(request):
    grupos = GrupoAlumnos.objects.filter(Usuario=request.user)
    juegos = Juego.objects.all()
    return render(request,'Alumnos/listaGruposUnidos.html',{'grupos':grupos,'juegos':juegos,})

@login_required(login_url='/login/')
def vista_salirDeGrupo(request,id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    grupoAlumno = GrupoAlumnos.objects.get(Usuario=request.user,Grupo=grupo)
    if grupoAlumno:
        grupoAlumno.delete()
        messages.success(request,"Has salido del grupo exitosamente")
    else:
        messages.success(request,"No se pudo salir del grupo")
    return redirect('gruposUnidos')

def vista_listaJuegosAlumnos(request,id_grupo):
    grupo=Grupo.objects.get(id=id_grupo)
    juegos = Juego.objects.filter(grupo=grupo)
    context = {'juegos':juegos,
                        'grupo':grupo}
    return render(request,'Alumnos/listaJuegosAlumno.html',context)
    pass
