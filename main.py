import pandas as pd

# 1. Importaciones corregidas con la lógica de tarifas
from notebook.consumo import consumir_tarifa
from notebook.limpieza import limpiar_datos
from notebook.tranformar import transform_data

# 2. Importación del módulo de gráficas
from notebook.graficas import (
    graficar_barras,
    graficar_lineas,
    graficar_mapa_calor,
    graficar_torta,
)

# 3. Flujo de datos de tu API
tarifas = consumir_tarifa()
tarifas_ordenadas = pd.DataFrame(tarifas)
tarifas_limpias = limpiar_datos(tarifas_ordenadas)
tarifas_transformadas = transform_data(tarifas_limpias)

print("Análisis completado con éxito. Generando gráficos...")

# =========================================================================
# GENERACIÓN DE GRÁFICOS
# =========================================================================

graficar_lineas(
    tarifas_transformadas["mensualidades_resumen"],
    columna_eje_x="tipo",
    columna_eje_y="cuenta",
    titulo="Resumen de Mensualidades (Tipo MES)",
    color_linea="#2196F3",
    nombre_archivo="lineas_mensualidades.png",
)

graficar_barras(
    tarifas_transformadas["promedio_activas"],
    columna_categorias="tipo",
    columna_valores="promedio_precio",
    titulo="Precio Promedio de Tarifas Activas por Tipo",
    color_barras="#4CAF50",
    nombre_archivo="barras_promedio_activas.png",
)

graficar_torta(
    tarifas_transformadas["distribucion_tipos"],
    columna_etiquetas="tipo",
    columna_valores="conteo_total",
    titulo="Proporción General de Tipos de Cobro",
    nombre_archivo="torta_distribucion_cobros.png",
)

graficar_mapa_calor(
    tarifas_transformadas["tarifas_premium"],
    columna_filas="tipo",
    columna_columnas="tipo",
    columna_valores="cuenta",
    titulo="Densidad de Tarifas Premium (>= 50k)",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_tarifas_premium.png",
)