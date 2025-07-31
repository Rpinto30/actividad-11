from math import trunc

proper = {}
error_mesagge = '-'*50+'\n'+"✖"*5+"   Lo siento, intentelo nuevamente   "+"✖"*5

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print(error_mesagge)
    return value

while True:
    n = input_integer("▶  Ingresa la cantidad de propietarios que deseas agreagar: ")
    if n > 0: break
    else: print(error_mesagge)

for i in range(n):
    while True:
        nit = input("▶  Ingrese su número de identificación (NIT): ")
        if nit in proper: print(error_mesagge)
        else: break

    name = input("▶  Ingrese su nombre completo: ")
    tel = input_integer("▶  Ingrese su número de teléfono: ")

    while True:
        c_cars = input_integer("▶  Ingrese la cantidad de vehículos que posee: ")
        if c_cars>0: break
        else: print(error_mesagge)

    cars = {}
    for j in range(c_cars):
        print("-"*10+f"VEHICULO {c_cars+1}"+"-"*10)
        plac = input("▶  Ingresa placa: ")
        marc = input("▶  Ingresa el nombre de la marca: ")
        model = input("▶  Ingresa el modelo del auto: ")
        year = input_integer("▶  Ingresa el año del vehiculo")

        while True:
            print("-" * 15 + '\n   1) Sí\n   2) No')
            imp_pay = input_integer("▶  Usted ha pagado su impuesto?: ")
            if 1<=imp_pay<= 2: break
            else: print(error_mesagge)
        cars[plac] = {
            'marca': marc,
            'model': model,
            'año': year
        }

    proper[nit]={

    }