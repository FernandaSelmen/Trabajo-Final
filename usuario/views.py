from django.shortcuts import render
from usuario.models import Texto
from usuario.forms import TextoForm

# Create your views here.

def inicio(request):
    return render(request, 'usuario/index.html')


def publicaciones(request):
    return render(request, 'usuario/publicaciones.html')


def mostrar(request):

    muestra = Texto.objects.all()

    return render(request, 'usuario/publicaciones.html', {'mostra': muestra})

def agregar(request):

    if request.method == 'POST':

        textox = TextoForm(request.POST)

        if textox.is_valid():

            data = textox.cleaned_data

            titulo = data['titulo']
            subtitulo = data['subtitulo']
            dia = data['dia']
            imagen = data['imagen']
            contenido = data['contenido']

            texto = Texto(titulo = titulo, subtitulo = subtitulo, dia = dia, imagen = imagen, contenido = contenido)

            texto.save()

            return render(request, 'usuario/publicaciones.html' )
    else:

        textox = TextoForm()

        return render(request, 'usuario/agregar.html', {'texto': textox})

def editar(request, id_texto):
 
    texto = Texto.objects.get(id = id_texto)

    if request.method == 'POST':

        textox = TextoForm(request.POST)

        if textox.is_valid():

            data = textox.cleaned_data

            texto.titulo = data['titulo']
            texto.subtitulo = data['subtitulo']
            texto.dia = data['dia']
            texto.imagen = data['imagen']
            texto.contenido = data['contenido']

            texto.save()

            return render(request, 'usuario/publicaciones.html' )
    else:
        textox = TextoForm()

        return render(request, 'usuario/editar.html', {'texto': textox})

def eliminar(request, id_texto):
    
    texto = Texto.objects.get(id = id_texto)
    
    titulo = texto.titulo

    texto.delete()

    return render(request, 'usuario/eliminar.html',{'titulo_eliminado': titulo} )

