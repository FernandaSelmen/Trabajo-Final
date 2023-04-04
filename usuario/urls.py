from django.urls import path
from usuario.views import inicio, publicaciones, mostrar, agregar, eliminar, editar




urlpatterns = [ 
    path('', inicio, name = 'inicio'),
    path('publicaciones/', publicaciones, name = 'publicaciones'),
    path('mostrar/', mostrar, name = 'mostrar'),
    path('editar/<int:id_texto>/', agregar, name = 'editar'),
    path('eliminar/<int:id_texto>/', eliminar, name = 'eliminar'),
    path('agregar/<int:id_texto>/', editar, name = 'agregar'),
      ]

