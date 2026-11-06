# config.py
# config.py
# Variables globales y configuración de red
DJANGO_BASE_URL = "http://127.0.0.1:8000/api/v1"
FASTAPI_BASE_URL = "http://127.0.0.1:8001"
TOKEN_JWT = None

def obtener_headers():
    import config
    if not config.TOKEN_JWT:
        return {"Content-Type": "application/json"}
    return {
        "Authorization": f"Bearer {config.TOKEN_JWT}",
        "Content-Type": "application/json"
    }