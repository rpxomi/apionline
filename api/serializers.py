from rest_framework import serializers
from .models import Producto, Tarjeta


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'titulo', 'descripcion', 'precio', 'imagen_url', 'categoria']


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ['id', 'encabezado', 'cuerpo']
