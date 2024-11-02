# Pagina-Bienes-Raices-
Aplicacion web para un negocio de bienes raices


# API

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas en tu máquina antes de comenzar:

- **Python 3.7+**
- **pip** (el gestor de paquetes de Python)
- **Virtualenv** (opcional pero recomendado)

# Crea entorno virtual
python -m venv venv

# Instala dependencias
pip install django
pip install django-cors-headers
pip install djangorestframework
pip install coreapi
pip install setuptools

# Ejecutar
python manage.py migrate
python manage.py runserver

