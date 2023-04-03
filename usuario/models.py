from django.db import models

# Create your models here.
class persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    texto = models.CharField()

