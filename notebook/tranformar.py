import pandas as pd

def transform_data(dataFrameLimpio):
    
    # Filtro 1: Análisis de Mensualidades
    # Usamos 'MES' para coincidir con el Enum de Java
    filtro1 = dataFrameLimpio.query("tipo == 'MES'")
    agrupacion1 = filtro1.groupby("tipo")["id"].count().reset_index(name="cuenta")
    
    # Filtro 2: Tarifas de Alto Valor (Costos >= 50,000)
    filtro2 = dataFrameLimpio.query("valor >= 50000")
    agrupacion2 = filtro2.groupby("tipo")["id"].count().reset_index(name="cuenta")
    
    # Filtro 3: Tarifas Activas (Campo 'activo' de Java)
    # Cambiamos 'estados' por 'activo' que es el nombre en tu Entity
    filtro3 = dataFrameLimpio.query("activo == True")
    agrupacion3 = filtro3.groupby("tipo")["valor"].mean().reset_index(name="promedio_precio")

    # Filtro 4: Distribución general de tipos de cobro
    # Ya que no hay 'categorias' en tu modelo Java, agrupamos por Tipo de Tarifa
    agrupacion4 = dataFrameLimpio.groupby("tipo")["id"].count().reset_index(name="conteo_total")

    # Filtro 5: Tarifas de Corta Estancia (HORA)
    # Usamos 'HORA' para coincidir con el Enum de Java
    filtro5 = dataFrameLimpio.query("tipo == 'HORA'")
    agrupacion5 = filtro5.groupby("tipo")["valor"].max().reset_index(name="maximo_valor")

    resultado = {
        "mensualidades_resumen": agrupacion1,
        "tarifas_premium": agrupacion2,
        "promedio_activas": agrupacion3,
        "distribucion_tipos": agrupacion4,
        "maximos_por_hora": agrupacion5
    }
    
    return resultado