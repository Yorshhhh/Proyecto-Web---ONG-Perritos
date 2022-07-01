from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'Mascota']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2',]