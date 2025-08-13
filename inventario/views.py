from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Categoria, Producto, Proveedor
from .serializers import CategoriaSerializer, ProductoSerializer, ProveedorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('categoria').all()
    serializer_class = ProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

@api_view(['GET'])
def stock_report(request):
    data = (Producto.objects
            .values('categoria__id', 'categoria__nombre')
            .annotate(total_stock=Sum('stock')))
    result = [{'categoria_id': d['categoria__id'], 'categoria': d['categoria__nombre'], 'total_stock': d['total_stock'] or 0} for d in data]
    return Response(result)
