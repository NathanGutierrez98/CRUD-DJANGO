from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completado = models.DateTimeField(null = True, blank=True)
    urgente = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo + ' ' +  self.usuario.username