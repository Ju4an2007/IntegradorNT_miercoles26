import requests

def consumir_tarifa():
    url = "http://localhost:8080/parkingsystem/v1/tarifas"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos