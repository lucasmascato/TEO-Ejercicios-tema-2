import csv
from datetime import datetime

def lee_variaciones_temperatura(fichero):
    with open(fichero, encoding="utf-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for fecha, variacion in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            variacion = float(variacion)
            tupla = (fecha, variacion)
            lista.append(tupla)

    return lista