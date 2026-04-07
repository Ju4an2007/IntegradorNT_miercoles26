import random
from datetime import datetime, timedelta

def simular_tarifas_parking(numeroTarifas):

    # defino atributos base
    tipos = ["POR_HORA", "POR_DIA", "POR_MES"]
    categorias = ["MOTO", "CARRO", "CAMIONETA", "BICICLETA"]
    estados = [True, False]

    # rango de fecha inicial
    fechaInicial = datetime(2026, 1, 1)
    
    # ciclo para generar N registros 
    tarifas = []
    for _ in range(numeroTarifas):
        # fecha aleatoria para cada registro
        fechaBase = fechaInicial + timedelta(days=random.randint(0, 180))
        
        tarifa = {
            "id": random.randint(1, 1000),
            "tipo": random.choice(tipos),
            "descripcion": f"Tarifa estándar para {random.choice(categorias)}",
            "valor": random.randint(2000, 250000),
            "fecha_creacion": fechaBase.strftime("%Y/%m/%d"),
            "activo": random.choice(estados)
        }
        tarifas.append(tarifa)
        
    return tarifas
