from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Context, Template 
from django.template import loader


# Create your views here.
def familia(request):

    mama = Familiares(nombre='Maria', apellido='Avila', edad=50, telefono=1165738834, email="maryavila@gmail.com", nacimiento= "1971-11-05")
    papa = Familiares(nombre='Guillermo', apellido='Zequeira', edad=51, telefono=1153960064, email="zequeguille@gmail.com", nacimiento="1970-11-19")
    hermana =Familiares(nombre='Milagros', apellido='Zequeira', edad=16, telefono=1183657735, email="milizeq@gmail.com", nacimiento="2005-10-10")
    hermano =Familiares(nombre="Leandro", apellido="Zequeira", edad=25, telefono=1153745867, email="zequeleandro@gmail.com", nacimiento="1997-03-11")
    mama.save()
    papa.save()
    hermana.save()
    hermano.save()
    texto_m =f'Hola mi nombre es {mama.nombre} {mama.apellido}, naci el {mama.nacimiento} y mi edad es {mama.edad}. Mi telefono e imail de contacto es {mama.telefono} {mama.email} en ese orden'
    texto_p =f'Hola mi nombre es {papa.nombre} {papa.apellido}, naci el {papa.nacimiento} y mi edad es {papa.edad}. Mi telefono e imail de contacto es {papa.telefono} {papa.email} en ese orden'
    texto_ha =f'Hola mi nombre es {hermana.nombre} {hermana.apellido}, naci el {hermana.nacimiento} y mi edad es {hermana.edad}. Mi telefono e imail de contacto es {hermana.telefono} {hermana.email} en ese orden'
    texto_ho =f'Hola mi nombre es {hermano.nombre} {hermano.apellido}, naci el {hermano.nacimiento} y mi edad es {hermano.edad}. Mi telefono e imail de contacto es {hermano.telefono} {hermano.email} en ese orden'
    diccionario = {"texto_m":texto_m,"texto_p":texto_p,"texto_ha":texto_ha, "texto_ho":texto_ho}
    miArchivo=open("C:/Users/zeque/Desktop/Python coder/Entregable/Entregable_1/Plantillas/template_1.html")
    contenido=miArchivo.read()
    miArchivo.close()
    plantilla=Template(contenido)
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)

    return HttpResponse(documento)