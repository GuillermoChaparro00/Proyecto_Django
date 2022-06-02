from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns=[


    path("",views.plantilla),
    path("alumnos",views.alumnos, name="alumnos"),
    path("profesores",views.profesores, name="profesores"),
    path("cargar_alumno",views.cargar_alumno, name="cargar_alumno"),
    path("buscar_alumno",views.buscar_alumno),
    path("buscar",views.buscar),
    path("cargar_profesores",views.cargar_profesores, name="cargar_profesores"),
    path("cargar_curso",views.cargar_curso, name="cargar_curso"),
    path("cursos",views.cursos, name="cursos"),
]