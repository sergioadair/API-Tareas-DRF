from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(max_length=500)
    estado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)