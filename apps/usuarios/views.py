from django.shortcuts import render,redirect
from apps.usuarios.forms import RegistrarForm,PerfilForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,get_user_model,login,logout
# Create your views here.

def vista_registrar(request):
    if request.user.is_authenticated():
        return redirect('alumnosIndex')
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        profile_form = PerfilForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user  = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username,password=password)
            login(request,new_user)
            profile_form = PerfilForm(request.POST, instance=request.user.profile)
            profile_form.save()
            messages.success(request,"Felicidades "+str(user.username)+", bienvenido")
            return redirect('alumnosIndex')
    else:
        form = RegistrarForm()
        profile_form = PerfilForm()
    context = {
    "form":form,
    "profile_form": profile_form
    }
    return render(request, "usuarios/registrarse.html", context)
def vista_login(request):
    form  = LoginForm(request.POST or None)
    context = {"form":form}
    if request.user.is_authenticated():
        return redirect('alumnosIndex')
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        print(request.user.is_authenticated())
        tipo = str(request.user.profile.tipo)
        if tipo=="A":
            return redirect('alumnosIndex')
        else:
            return redirect('maestrosIndex')
    return render(request,"usuarios/login.html",context)
def vista_logout(request):
    logout(request)
    return redirect('login')
