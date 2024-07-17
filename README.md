# Django REST API para Gestión de Música

Este proyecto es una demostración de cómo desarrollar una API con Django y Django REST Framework para gestionar información relacionada con géneros musicales, artistas, álbumes y canciones. Puedes ver una explicación en detalle de todo el proceso en el blog de mi web: [nestorjimeno.com/blog](https://nestorjimeno.com/blog/creacion-de-apis-con-django-rest-framework/).

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
cd musicapi
python manage.py makemigrations
python manage.py migrate
```

Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

Una vez que el servidor de desarrollo está activado, podrás ver la API en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso

Puedes acceder a las siguientes endpoints de la API:

- /api/generos/ - Listar y crear géneros musicales
- /api/artistas/ - Listar y crear artistas
- /api/albums/ - Listar y crear álbumes
- /api/canciones/ - Listar y crear canciones

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejorar el proyecto.
