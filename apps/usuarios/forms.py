from django.contrib.auth import authenticate,get_user_model,login,logout
from django import forms
from django.contrib.auth.models import User
from apps.usuarios.models import Profile
class RegistrarForm(forms.ModelForm):
    username=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Correo",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password',
        'password2'
        ]
    def clean(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return super(RegistrarForm,self).clean(*args,**kwargs)

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    def clean(self,*args,**kwargs):
        user = authenticate(username=self.cleaned_data.get('username'),password=self.cleaned_data.get('password'))
        if not user:
            raise forms.ValidationError("El usuario o contraseña son incorrectos")
        return super(LoginForm,self).clean(*args,**kwargs)



class PerfilForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidoMaterno = forms.CharField(label="Apellido materno",widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidoPaterno = forms.CharField(label="Apellido paterno",widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo = forms.CharField(widget=forms.Select(attrs={'class':'form-control'},choices=(('M', 'Masculino'),('F', 'Femenino'),)))
    tipo = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=(('A', 'Alumno'),('M', 'Maestro'),)))
    class Meta:
        model = Profile
        fields=[
        'nombre',
        'apellidoMaterno',
        'apellidoPaterno',
        'sexo',
        'tipo'
        ]
