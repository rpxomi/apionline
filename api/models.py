from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # 9999999.99
    imagen_url = models.URLField(max_length=200) # blank es para el formulario y null para la base de datos
    categoria = models.CharField(max_length=6)

    def __str__(self):
        return self.titulo