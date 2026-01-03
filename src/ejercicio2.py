def extrae_numeros(texto: str)-> list[int]:
    numeros=[]
    for token in texto.split():
        try:
            numeros.append(int(token))
        except ValueError:
            pass
    return numeros
