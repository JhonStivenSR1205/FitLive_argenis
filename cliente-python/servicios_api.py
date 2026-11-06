# servicios_api.py
# Capa de conexión con Django y FastAPI
import requests
import config

def registrar_usuario_django(usuario, clave, correo):
    url = f"{config.DJANGO_BASE_URL}/auth/registro/"
    payload = {"username": usuario, "password": clave, "email": correo}
    return requests.post(url, json=payload, timeout=5)

def login_django(usuario, clave):
    return requests.post(f"{config.DJANGO_BASE_URL}/auth/login/", json={"username": usuario, "password": clave}, timeout=5)

def listar_rutinas():
    return requests.get(f"{config.DJANGO_BASE_URL}/rutinas/", headers=config.obtener_headers(), timeout=5)

def crear_rutina(payload):
    return requests.post(f"{config.DJANGO_BASE_URL}/rutinas/", json=payload, headers=config.obtener_headers(), timeout=5)

def crear_ejercicio(payload):
    return requests.post(f"{config.DJANGO_BASE_URL}/ejercicios/", json=payload, headers=config.obtener_headers(), timeout=5)

def analizar_salud_ia(payload):
    return requests.post(f"{config.FASTAPI_BASE_URL}/analizar-salud", json=payload, timeout=5)