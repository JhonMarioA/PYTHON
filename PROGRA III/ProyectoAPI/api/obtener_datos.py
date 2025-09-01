from sodapy import Socrata

def conectar_api(departamento, cantidad_de_registros):
    
    cliente = Socrata("www.datos.gov.co", None)

    registros = cliente.get("gt2j-8ykr", limit = cantidad_de_registros, where = f"departamento_nom = '{departamento}'")

    return registros