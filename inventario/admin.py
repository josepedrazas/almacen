from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Movimiento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sku', 'categoria', 'stock', 'precio')
    search_fields = ('nombre', 'sku')

admin.site.register(Proveedor)
admin.site.register(Movimiento)
