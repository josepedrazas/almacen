from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def clean(self):
        if self.precio is not None and self.precio < 0:
            raise ValidationError({'precio': 'El precio no puede ser negativo.'})
        if self.stock is not None and self.stock < 0:
            raise ValidationError({'stock': 'El stock no puede ser negativo.'})

    def __str__(self):
        return f"{self.nombre} ({self.sku})"

class Movimiento(models.Model):
    TIPO_CHOICES = (('ENTRADA', 'Entrada'), ('SALIDA', 'Salida'))
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    nota = models.CharField(max_length=255, blank=True)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': 'La cantidad debe ser mayor que 0.'})
        if self.fecha and self.fecha > timezone.now():
            raise ValidationError({'fecha': 'La fecha no puede estar en el futuro.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        if self.tipo == 'ENTRADA':
            self.producto.stock += self.cantidad
        else:
            self.producto.stock -= self.cantidad
        if self.producto.stock < 0:
            raise ValidationError('Stock negativo no permitido.')
        self.producto.save()
