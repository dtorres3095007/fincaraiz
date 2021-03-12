# fincaraiz

## Configuración Entorno Virtual

Crear entorno virtual

```bash
python -m venv prueba
```

activar entorno virtual

```bash
cd prueba
cd Scripts
activate
```

## Configuración Proyecto

Clonar el proyecto

```bash
git clone https://github.com/dtorres3095007/fincaraiz.git
```

Entrar a la carpeta del proyecto e instalar los requisitos

```bash
pip install -r requirements.txt
```

Crear Migraciones

```bash
python manage.py makemigrations
```

Ejecutar Migraciones

```bash
python manage.py migrate
```
Crear usuario admin

```bash
python manage.py createsuperuser
```

Ejecutar El servidor

```bash
python manage.py runserver
```
## Rutas Disponibles

Reviews
```bash
GET : http://127.0.0.1:8000/api/v1.0/reviews
```
```bash
POST : http://127.0.0.1:8000/api/v1.0/reviews/add
```
```bash
PUT AND DELETE : http://127.0.0.1:8000/api/v1.0/reviews/PK
```
