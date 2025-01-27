from django.urls import path
from .views import ProductoViewSet

urlpatterns = [
    path('productos/', ProductoViewSet.as_view({'get':'list'}), name='productos'),
    path('productos/<int:pk>/', ProductoViewSet.as_view({'get':'retrieve'}), name='producto'),
    path('productos/<str:categoria>/', ProductoViewSet.as_view({'get':'list'}), name='productos_categoria')
]