import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Permite importar desde ../modelo-ia/ cuando esté en el repositorio completo
RUTA_MODELO_IA = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modelo-ia"))
if RUTA_MODELO_IA not in sys.path:
    sys.path.append(RUTA_MODELO_IA)

try:
    from analizador import evaluar_salud_usuario
except ImportError:
    # Respaldo local por si se ejecuta la carpeta microservicio-fastapi de forma aislada
    def evaluar_salud_usuario(peso: float, estatura: float, calorias_consumidas: float, nivel_actividad: str = "moderado") -> dict:
        imc = round(peso / (estatura ** 2), 2)
        clasificacion = "Peso normal" if 18.5 <= imc < 25 else ("Bajo peso" if imc < 18.5 else "Sobrepeso/Obesidad")
        gasto = round(peso * 32.0, 2)
        balance = round(calorias_consumidas - gasto, 2)
        estado = "Balance equilibrado" if -300 <= balance <= 300 else ("Déficit calórico" if balance < -300 else "Superávit calórico")
        return {
            "imc": imc,
            "clasificacion_imc": clasificacion,
            "gasto_calorico_estimado": gasto,
            "balance_calorico": balance,
            "estado_balance": estado,
            "recomendacion": "Mantener hidratación y seguir la rutina activa registrada en FitLive."
        }

app = FastAPI(
    title="FitLive - Microservicio de Análisis e IA",
    version="1.0.0"
)

class SolicitudAnalisisSalud(BaseModel):
    peso: float = Field(..., gt=0, example=75.5)
    estatura: float = Field(..., gt=0, le=2.5, example=1.75)
    calorias_consumidas: float = Field(..., ge=0, example=2200.0)
    nivel_actividad: str = Field(default="moderado", example="moderado")

class RespuestaAnalisisSalud(BaseModel):
    imc: float
    clasificacion_imc: str
    gasto_calorico_estimado: float
    balance_calorico: float
    estado_balance: str
    recomendacion: str

@app.get("/health")
def verificar_estado():
    return {"status": "ok", "servicio": "microservicio-fastapi", "puerto": 8001}

@app.post("/analizar-salud", response_model=RespuestaAnalisisSalud)
def analizar_salud(datos: SolicitudAnalisisSalud):
    resultado = evaluar_salud_usuario(
        peso=datos.peso,
        estatura=datos.estatura,
        calorias_consumidas=datos.calorias_consumidas,
        nivel_actividad=datos.nivel_actividad
    )
    return resultado