def evaluar_salud_usuario(
    peso: float,
    estatura: float,
    calorias_consumidas: float,
    nivel_actividad: str = "moderado"
) -> dict:
    imc = round(peso / (estatura ** 2), 2)

    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25.0:
        clasificacion = "Peso normal"
    elif imc < 30.0:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    factores = {
        "sedentario": 26.0,
        "ligero": 29.0,
        "moderado": 32.0,
        "intenso": 36.0
    }
    factor = factores.get(nivel_actividad.lower().strip(), 32.0)
    gasto_estimado = round(peso * factor, 2)
    balance = round(calorias_consumidas - gasto_estimado, 2)

    if balance < -300:
        estado_balance = "Déficit calórico marcado"
        recomendacion = "Aumentar ingesta proteica para proteger masa muscular durante el déficit."
    elif -300 <= balance <= 300:
        estado_balance = "Balance calórico equilibrado"
        recomendacion = "Excelente equilibrio energético. Mantener la rutina activa programada."
    else:
        estado_balance = "Superávit calórico"
        recomendacion = "Incrementar sesiones cardiovasculares o ajustar porciones calóricas del día."

    return {
        "imc": imc,
        "clasificacion_imc": clasificacion,
        "gasto_calorico_estimado": gasto_estimado,
        "balance_calorico": balance,
        "estado_balance": estado_balance,
        "recomendacion": recomendacion
    }


if __name__ == "__main__":
    resultado_prueba = evaluar_salud_usuario(
        peso=75.5,
        estatura=1.75,
        calorias_consumidas=2200.0,
        nivel_actividad="moderado"
    )
    print("=== PRUEBA DEL MODELO DE IA FITLIVE ===")
    for clave, valor in resultado_prueba.items():
        print(f"{clave}: {valor}")