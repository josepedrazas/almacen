from django.test import TestCase
from rest_framework.test import APIClient
from .models import Categoria, Producto

class ModeloValidacionTest(TestCase):
    def test_producto_precio_no_negativo(self):
        cat = Categoria.objects.create(nombre='Test')
        p = Producto(categoria=cat, nombre='P', sku='SKU1', precio=-5, stock=10)
        with self.assertRaises(Exception):
            p.full_clean()

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.cat = Categoria.objects.create(nombre='CatA')
        Producto.objects.create(categoria=self.cat, nombre='Prod1', sku='S1', precio=10, stock=5)
        Producto.objects.create(categoria=self.cat, nombre='Prod2', sku='S2', precio=20, stock=3)

    def test_list_productos(self):
        resp = self.client.get('/api/productos/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 2)

    def test_stock_report(self):
        resp = self.client.get('/api/stock-report/')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['total_stock'], 8)
