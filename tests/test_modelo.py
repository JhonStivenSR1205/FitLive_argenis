import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modelo-ia")))

from analizador import evaluar_salud_usuario

def test_evaluar_salud_usuario():
    resultado = evaluar_salud_usuario(75.5, 1.75, 2200.0, "moderado")
    assert resultado["imc"] == 24.65
    assert resultado["clasificacion_imc"] == "Peso normal"
    assert "gasto_calorico_estimado" in resultado
    assert "balance_calorico" in resultado
    assert "estado_balance" in resultado
    assert "recomendacion" in resultado
    print("Prueba unitaria de IA pasada con éxito.")

if __name__ == "__main__":
    test_evaluar_salud_usuario()