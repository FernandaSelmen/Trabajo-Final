from django.db import models

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    def __str__(self):
         
         return f'nombre: {self.nombre} - apellido: {self.apellido} - correo: {self.correo} '
   
class Texto(models.Model):
    
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=100)
    dia = models.DateField()
    imagen = models.ImageField()
    contenido = models.TextField()

    def __str__(self):
         
         return f'titulo: {self.titulo} - dia: {self.dia}'


