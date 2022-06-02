from django import forms

class Alumnos_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    edad=forms.IntegerField()
    dni=forms.IntegerField()
    nacimiento=forms.DateField()

class Curso_formulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    camada=forms.IntegerField()
    turno=forms.CharField(max_length=15)