from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Personas , Profesores , Curso
 
from django.template import loader
from app_coder.forms import Alumnos_formulario,  Curso_formulario

# Create your views here.
def verPersonas(request):
    lasper=Personas.objects.all()
    diccionario={"Personas": lasper}
    platilla=loader.get_template("verPersonas.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)


def alta_Persona(request):
    persona= Personas(nombre="Nicolas",apellido="Faria",edad=47,dni=386374846, nacimiento="2001-4-6")
    persona.save()
    text= f"Persona:{persona.nombre} Edad:{persona.edad} se guardo en la BD"
    return HttpResponse(text)

def cargar_Persona(request):

    if request.method=="POST":
        persona= Personas(nombre= request.POST["nombre"],apellido="Chaparro",edad=26,dni=2387535)
        persona.save()
    return render(request, "cargarPersona.html")









def plantilla(request):
    return render(request, "plantilla.html")

##ALUMNOOS
def alumnos(request):
    los_alumnos=Personas.objects.all()
    diccionario={"alumnos": los_alumnos}
    platilla=loader.get_template("alumnos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)

def cargar_alumno(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            persona= Personas(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            persona.save()
    return render(request, "cargar_alumno.html")

def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"] 
        alumnos=Personas.objects.filter(nombre__icontains =nombre)
        return render(request,"resultado_busqueda.html",{"alumnos":alumnos})
    else:
        return HttpResponse("campo vacio")
##fin alumnos


##PROFESORES 
def cargar_profesores(request):
    if request.method=="POST":
        validacionForm=Alumnos_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            Profe= Profesores(nombre= datos["nombre"],apellido=datos["apellido"],edad=datos["edad"],dni=datos["dni"],nacimiento=datos["nacimiento"])
            Profe.save()
    return render(request, "cargar_profesores.html")

def profesores(request):
    los_profes=Profesores.objects.all()
    diccionario={"profesores": los_profes}
    platilla=loader.get_template("profesores.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)  

##FIN PROFESORES

##CURSOS
def cargar_curso(request):
    if request.method=="POST":
        validacionForm= Curso_formulario(request.POST)
        
        if validacionForm.is_valid():
            datos=validacionForm.cleaned_data
            cursos= Curso(nombre= datos["nombre"],camada=datos["camada"],turno=datos["turno"])
            cursos.save()
    return render(request, "cargar_curso.html")

def cursos(request):
    los_cursos=Curso.objects.all()
    diccionario={"cursos": los_cursos}
    platilla=loader.get_template("cursos.html")
    documento=platilla.render(diccionario)
    return HttpResponse(documento)  
##FIN CURSOS