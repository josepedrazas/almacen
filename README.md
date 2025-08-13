# 📦 Sistema de Almacenes en Django

Este es un sistema básico de gestión de almacenes desarrollado en **Django** y **SQLite**, sin autenticación, ideal para entornos locales o pruebas rápidas.

## 🚀 Características
- CRUD de **Categorías**
- CRUD de **Productos**
- CRUD de **Proveedores**
- Endpoints REST con Django REST Framework
- Base de datos **SQLite**
- Carga de datos de prueba con `loaddata`
- Tests automatizados

---

## 📂 Instalación

### 1️⃣ Clonar git clone https://github.com/josepedrazas/almacen.git
git clone https://github.com/josepedrazas/almacen.gitel
```bash
cd almacen
```

### 2️⃣ Crear entorno virtual
```bash
python -m venv venv
```

Activar entorno:
- **Windows**
```bash
venv\Scripts\activate
```
- **Linux / Mac**
```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 🗄 Configuración de la base de datos
Este proyecto usa **SQLite** por defecto.

1. Crear las migraciones:
```bash
python manage.py makemigrations inventario
```

2. Aplicar migraciones:
```bash
python manage.py migrate
```

---

## 🧪 Cargar datos de prueba
El proyecto incluye un archivo `datos.json` con información de ejemplo.

```bash
python manage.py loaddata datos.json
```

---

## ▶️ Ejecutar el servidor
```bash
python manage.py runserver
```
Abrir en el navegador:  
```
http://127.0.0.1:8000
```

---

## 📡 Endpoints principales
| Método | URL                          | Descripción                    |
|--------|------------------------------|---------------------------------|
| GET    | `/categorias/`               | Listar categorías              |
| POST   | `/categorias/`               | Crear categoría                |
| GET    | `/productos/`                | Listar productos               |
| POST   | `/productos/`                | Crear producto                 |
| GET    | `/proveedores/`               | Listar proveedores             |
| POST   | `/proveedores/`               | Crear proveedor                |
| GET    | `/productos-bajo-stock/`     | Listar productos con bajo stock |

---

## 🧪 Ejecutar tests
```bash
python manage.py test
```

---

## 📌 Notas
- No requiere autenticación.
- Base de datos SQLite (`db.sqlite3`) incluida para uso local.
- Compatible con **Python 3.10+**.

---
