"""jueguito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from apps.alumnos.views import *
from apps.usuarios.views import *
from apps.teacher.views import *
from apps.groups.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alumnosindex/',alumnosIndex,name='alumnosIndex'),
    url(r'^unirseGrupo/',vista_GrupoAlumnos,name='unirseGrupo'),
    url(r'^maestrosIndex/',alumnosIndex,name='maestrosIndex'),
    url(r'^crearGrupo/',vista_Grupos,name='crearGrupo'),
    url(r'^api-data/(?P<id_grupo>\d+)/$',ChartData.as_view,name='api-data'),
    url(r'^graficasMaestros/(?P<id_grupo>\d+)/$',vista_graficasMaestros,name='graficasMaestros'),
    url(r'^graficasAlumnos/(?P<id_juego>\d+)/$',vista_graficasAlumnos,name='graficasAlumnos'),
    url(r'^crearJuego/(?P<id_grupo>\d+)/$',vista_juego_agregar,name='crearJuego'),
    url(r'^resultadosAlumno/(?P<id_grupo>\d+)/$',vista_listaResultadosAlumnos,name='resultadosAlumno'),
    url(r'^resultadosGrupo/(?P<id_grupo>\d+)/$',vista_listaResultadosGrupos,name='resultadosGrupo'),
    url(r'^resultados/(?P<cadena>.*)/$',vista_resultadosAlumnos,name='resultados'),
    url(r'^eliminarJuego/(?P<id_juego>\d+)/$',visa_juego_eliminar,name='eliminarJuego'),
    url(r'^salirGrupo/(?P<id_grupo>\d+)/$',vista_salirDeGrupo,name='salirGrupo'),
    url(r'^listaJuegos/(?P<id_grupo>\d+)/$',vista_lista_juegos,name='listaJuegos'),
    url(r'^listaJuegosAlumno/(?P<id_grupo>\d+)/$',vista_listaJuegosAlumnos,name='listaJuegosAlumno'),
    url(r'^listaGrupoAlumnos/(?P<id_grupo>\d+)/$',vista_lista_GrupodeAlumnos,name='grupoAlumnos'),
    url(r'^listaGrupos/',lista_grupos,name='listaGrupos'),
    url(r'^gruposUnidos/',vista_ListaGruposUnidos,name='gruposUnidos'),
    url(r'^login/',vista_login,name='login'),
    url(r'^logout/',vista_logout,name='logout'),
    url(r'^juego/(?P<id_grupo>\d+)/(?P<id_juego>\d+)/$',juego,name='juego'),
    url(r'^registrarse/',vista_registrar,name='registrarse'),
]
