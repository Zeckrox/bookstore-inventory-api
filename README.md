# Bookstore Inventory API

API REST para un sistema de gestión de inventario de librerías que incluye validación de precios en tiempo real.

## Tecnologías utilizadas
- **Python 3.x**  
- **Django 4.x**  
- **Django REST Framework** 
- **Dotenv**  
- **SQLite** (base de datos por defecto)  
- **Docker** (opcional )  
- **Requests** (para integración con API de tasas de cambio)

---

## Requisitos previos
- Python 3.9 o superior  
- pip o pipenv  
- Docker (opcional)  
- Conexion a internet para obtener tasas de cambio  

---

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/Zeckrox/bookstore-inventory-api.git
cd bookstore-inventory-api
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
O usando pipenv:
```bash
pipenv install
pipenv shell
```

### 3. Aplicar migraciones
```bash
python manage.py migrate
```

### 4. Ejecutar la API
```bash
python manage.py runserver
```
La API estará disponible en:  
```
http://127.0.0.1:8000/
```

---

## Usando Docker (opcional)

### Levantar contenedor
```bash
docker-compose up --build
```
La API estará disponible en:  
```
http://localhost:8000/
```

---

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|---------|-------------|
| POST   | /books  | Crear un libro |
| GET    | /books  | Listar todos los libros |
| GET    | /books?page=1  | Listar todos los libros con paginacion|
| GET    | /books/{id} | Obtener libro por ID |
| PUT    | /books/{id} | Actualizar libro |
| DELETE | /books/{id} | Eliminar libro |
| GET    | /books/search?category={category} | Buscar por categoría |
| GET    | /books/low-stock?threshold=10 | Libros con stock bajo |
| POST   | /books/{id}/calculate-price | Calcular precio de venta sugerido usando tasa de cambio actual |

---

## Colección de Postman
Se incluye archivo `BookstoreInventoryApi.postman_collection.json` con todos los endpoints.

