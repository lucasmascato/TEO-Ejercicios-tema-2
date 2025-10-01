def es_bisiesto(año):
    return año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)

def extrae_numeros(frase):
    lista = frase.strip().split()
    res  = []
    for cadena in lista:
        if cadena.isdigit():
            res.append(int(cadena))
    return res

