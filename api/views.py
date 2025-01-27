from rest_framework.viewsets import ModelViewSet
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria = self.kwargs.get('categoria', None)
        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)
        return queryset