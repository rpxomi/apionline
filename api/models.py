from django.db import models


# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # 9999999.99
    imagen_url = models.URLField(max_length=200) # blank es para el formulario y null para la base de datos
    categoria = models.CharField(max_length=6)

    def __str__(self):
        return self.titulo


# debería haber una tabla Categoria, para usar una clave foránea
# y no repetir el campo "categoria" en esta tabla Tarjeta
class Tarjeta(models.Model):
    encabezado = models.CharField(max_length=6)
    cuerpo = models.TextField(max_length=200)

    def __str__(self):
        return self.encabezado
