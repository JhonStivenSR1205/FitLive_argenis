# FitLive - Plataforma Integral de Salud y Entrenamiento

FitLive es un sistema evolutivo desarrollado en Python que gestiona el entrenamiento, la nutrición y las métricas físicas de sus usuarios mediante una arquitectura de microservicios y un modelo de IA.

## Requisitos y Configuración Inicial

El proyecto está diseñado para funcionar con las siguientes tecnologías:
*   Python 3.10 o superior
*   Microsoft SQL Server (Base de datos relacional)
*   Django y Django REST Framework
*   FastAPI
*   Requests (para el cliente)

## Estructura del Proyecto

El repositorio está dividido en 5 componentes principales según los lineamientos arquitectónicos:

1.  `api-django/`: Backend principal con la base de datos SQL Server y autenticación JWT.
2.  `microservicio-fastapi/`: Microservicio para cálculos y diagnósticos en tiempo real.
3.  `modelo-ia/`: Algoritmo de predicción de estado físico y cálculo calórico.
4.  `cliente-python/`: Aplicación cliente que consume todas las APIs.
5.  `tests/`: Pruebas unitarias para integración continua (CI/CD).

## Instrucciones de Ejecución

Para iniciar el sistema completo, se deben levantar los servicios en este orden estricto:

### 1. Iniciar la API Principal (Django)
```bash
cd api-django
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver 8000