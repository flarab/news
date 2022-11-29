# Tarea 5

Crear interface en flutter que consuma los siguientes servicios.

La aplicación debe listas los registros, crear registros que deben contener un título, body, imagen principal
y galería de imágenes.


Para correr localmente, se necesita al menos una base sqlite

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Listar registros GET
```
http://0.0.0.0:8080/api/news/
```

### Crear registro POST

```
http://0.0.0.0:8080/api/news/

Ejemplo

{
    "id": 1,
    "title": "test",
    "body": "test",
    "tags": [],
    "main_image": "http://0.0.0.0:8080/news/crc3.png",
    "created_at": "2022-11-28T23:06:37.141967Z",
    "updated_at": "2022-11-28T23:06:37.141997Z",
    "images": []
}


```

### Editar registro PUT

```
http://0.0.0.0:8080/api/news/{id}/
```

### Eliminar registro DELETE

```
http://0.0.0.0:8080/api/news/{id}/
```
