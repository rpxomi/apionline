from rest_framework.viewsets import ModelViewSet
from .models import Producto, Tarjeta
from .serializers import ProductoSerializer, TarjetaSerializer


class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria = self.kwargs.get('categoria', None)
        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)
        return queryset


class TarjetaViewSet(ModelViewSet):
    serializer_class = TarjetaSerializer

    def get_queryset(self):
        queryset = Tarjeta.objects.all()
        encabezado = self.kwargs.get('encabezado', None)
        if encabezado is not None:
            queryset = queryset.filter(encabezado=encabezado)
        return queryset
