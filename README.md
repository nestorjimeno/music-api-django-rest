# Django REST API para Gestión de Música

Este proyecto es una demostración de cómo desarrollar una API con Django y Django REST Framework para gestionar información relacionada con géneros musicales, artistas, álbumes y canciones. Puedes ver una explicación en detalle de todo el proceso en el blog de mi web: [nestorjimeno.com/blog](https://nestorjimeno.com/blog/creacion-de-apis-con-django-rest-framework/)

## Características

- Gestión de géneros musicales
- Gestión de artistas y sus biografías
- Gestión de álbumes y sus artistas y géneros asociados
- Gestión de canciones, incluyendo su duración, álbum, artistas y géneros asociados

## Estructura del Proyecto

### `admin.py`

Define cómo los modelos serán administrados en el panel de administración de Django.

### `models.py`

Define los modelos para géneros musicales, artistas, álbumes y canciones.

### `serializers.py`

Define los serializadores para convertir los modelos en formatos JSON.

### `views.py`

Define las vistas para manejar las operaciones de creación y listado de los modelos.

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/nestorjimeno/music-api-django-rest.git
```

2. Navega al directorio del proyecto:

```bash
cd music-api-django-rest
```

3. Crea un entorno virtual:

```bash
python -m venv venv
```

4. Activa el entorno virtual:

- En Windows:

```bash
venv\Scripts\activate
```

- En macOS/Linux:

```bash
source venv/bin/activate
```

5. Instala las dependencias:

```bash
pip install -r requirements.txt
```

Realiza las migraciones de la base de datos:

```bash
python manage.py migrate
```

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

## Uso

Puedes acceder a las siguientes endpoints de la API:

- /api/generos/ - Listar y crear géneros musicales
- /api/artistas/ - Listar y crear artistas
- /api/albums/ - Listar y crear álbumes
- /api/canciones/ - Listar y crear canciones

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejorar el proyecto.
