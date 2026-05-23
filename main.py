# Microservicio de café - FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Recolector(BaseModel):
    nombre: str
    kilos_diarios: List[int]

@app.post("/liquidar-pago")
def liquidar_pago(datos: Recolector):

    total_kilos = 0

    # Ciclo for para sumar kilos
    for kilo in datos.kilos_diarios:
        total_kilos += kilo

    pago_base = total_kilos * 600

    bono = 0

    # Condicionales para bonos
    if total_kilos > 150:
        bono = 50000
    elif total_kilos > 100:
        bono = 20000
    else:
        bono = 0

    pago_total = pago_base + bono

    return {
        "nombre": datos.nombre,
        "total_kilos": total_kilos,
        "pago_base": pago_base,
        "bono": bono,
        "pago_total": pago_total
    }