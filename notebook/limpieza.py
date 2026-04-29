import pandas as pd

def limpiar_tarifas_parking(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()


    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].astype("string").str.strip().str.upper() 
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype("string").str.strip().str.lower() 

  
    valores_esperados_tipos = ["POR_HORA", "POR_DIA", "POR_MES"]
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(valores_esperados_tipos),
        pd.NA
    )

   
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"])

   
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 0]

   
    data_frame_limpio["fecha_creacion"] = pd.to_datetime(data_frame_limpio["fecha_creacion"])

   
    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha_creacion"] = data_frame_limpio["fecha_creacion"].fillna(fecha_default)


    columnas_obligatorias = ["id", "tipo", "valor", "fecha_creacion"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio