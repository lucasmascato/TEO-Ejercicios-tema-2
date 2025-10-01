from datetime import date

def calcula_edad(fecha_nacimiento):
    hoy = date.today()

    fecha_cumpleaños = date(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)
    edad = hoy.year - fecha_nacimiento.year
    if hoy < fecha_cumpleaños:
        edad -= 1
    
    if hoy > fecha_cumpleaños:
        proximo_cumpleaños = date(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)
    else:
        proximo_cumpleaños = fecha_cumpleaños
    dias = (proximo_cumpleaños - hoy).days

    return edad, dias