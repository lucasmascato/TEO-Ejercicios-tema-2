from datetime import date

def calcula_edad(año: int, mes: int, dia: int):
    fecha = date(año, mes, dia)
    hoy = date.today()
    edad = hoy.year - fecha.year - ((hoy.month, hoy.day) < (mes, dia))
    cumpleaños = date(hoy.year, fecha.month, fecha.day)
    diferencia =  (cumpleaños - hoy).days
    print(f'Tienes {edad} años. Faltan {diferencia} días para tu cumpleaños')
