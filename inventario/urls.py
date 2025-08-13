from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoriaViewSet, ProductoViewSet, ProveedorViewSet, stock_report

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stock-report/', stock_report, name='stock-report'),
]
