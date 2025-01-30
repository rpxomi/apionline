from django.urls import path
from .views import ProductoViewSet, TarjetaViewSet


urlpatterns = [
    path('productos/', ProductoViewSet.as_view({'get':'list'}), name='productos'),
    path('productos/<int:pk>/', ProductoViewSet.as_view({'get':'retrieve'}), name='producto'),
    path('productos/<str:categoria>/', ProductoViewSet.as_view({'get':'list'}), name='productos_categoria'),

    path('tarjetas/', TarjetaViewSet.as_view({'get':'list'}), name='tarjetas'),

    # retrieve es solo con pk (primary key) clave primaria, o sea el id numerico
    path('tarjetas/<str:encabezado>/', TarjetaViewSet.as_view({'get':'list'}), name='tarjeta'),
]
