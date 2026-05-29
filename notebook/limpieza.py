import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].astype("string").str.strip().str.upper() 
    
    
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].str.replace("POR_", "", regex=False)
    
    valores_esperados_tipos = ["HORA", "DIA", "MES"]
    data_frame_limpio["tipo"] = data_frame_limpio["tipo"].where(
        data_frame_limpio["tipo"].isin(valores_esperados_tipos),
        pd.NA
    )

    
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors='coerce')
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"], errors='coerce')

   
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 0]

  
    if "activo" in data_frame_limpio.columns:
        data_frame_limpio["activo"] = data_frame_limpio["activo"].astype(bool)

   
    columnas_obligatorias = ["id", "tipo", "valor"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio