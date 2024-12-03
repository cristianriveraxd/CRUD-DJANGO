
# CRUD de Biblioteca con Django y SQLite



## Descripción

Este proyecto es un sistema CRUD (Crear, Leer, Actualizar, Eliminar) desarrollado con el framework Django, Bootstrap para manejar el Front-End y utilizando SQLite como base de datos. Permite gestionar los registros de una biblioteca, incluyendo la creación de libros, edición de sus datos, eliminación de registros y la visualización de una lista con funciones de búsqueda.
## Requisitos del Sistema

- Python 3.8 o superior
- Pip (Administrador de paquetes de Python)
- Django 4.x o superior
- Sistema operativo compatible (Windows, macOS o Linux)
## Instrucciones de instalación

Clona este repositorio en tu máquina local:

```bash
  git clone https://github.com/tuusuario/crud-biblioteca-django.git

```

Navega al directorio del proyecto

```bash
  cd crud-biblioteca-django
```

Configura tu entorno virtual

```bash
  python -m venv venv

```

Activa el entorno virtual

```bash
  - Windows:
  venv\Scripts\activate

  - macOS/Linux:
  source venv/bin/activate
```


## Instalación de dependencias

 Asegurate que tu entorno virtual este activo e instala las dependencias requeridas:
```bash
  pip install -r requirements.txt
```
## Instrucciones para ejecutar el proyecto

 Realiza las migraciones iniciales de la base de datos:
```bash
  python manage.py migrate
```
 Inicia el servidor de desarrollo:
```bash
  python manage.py runserver
```
 Abre tu navegador y accede a la URL:
```bash
  http://127.0.0.1:8000/
```

## Principales funcionalidades

### Pagina principal

![image](https://github.com/user-attachments/assets/73c1e75a-aa8a-491d-8c4c-1788429adf1a)

### Añadir nuevos libros

![image](https://github.com/user-attachments/assets/bcf91cc7-52ff-4dda-b928-fdd512ef2d54)

![image](https://github.com/user-attachments/assets/751f993b-1d92-49bc-bc17-d19726ebb3a7)

### Validación de datos

![image](https://github.com/user-attachments/assets/ab281ba1-8367-4fa0-af84-3cce74f93e3c)

### Funcionalidad de actualizar la información de los libros y facilidad para eliminar libros

![image](https://github.com/user-attachments/assets/08433707-9e14-4043-b053-a6d10a605b9d)

### Interfaz de editar libros

![image](https://github.com/user-attachments/assets/b8109f69-b8dc-45ee-83ff-5b2d3d420ea4)

### Interfaz de eliminar libros

![image](https://github.com/user-attachments/assets/49654ba4-639f-43cb-a1bb-c3fb400e9557)

### Facilidad para filtar por titulos de libros

![image](https://github.com/user-attachments/assets/947c622e-de76-4c7a-aee3-723d7e552ba4)

### Filtrar libro Harry Potter

![image](https://github.com/user-attachments/assets/a88dde8a-5907-4389-a324-29268cbb5f8d)



## Información de contacto

Si tienes preguntas o deseas contribuir al proyecto, puedes contactarnos a través de:
- GitHub: https://github.com/cristianriveraxd
