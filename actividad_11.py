proper = {'123456789': {'name': 'pANL', 'tel': 12345678,
                        'cars': [{'plac': 'asd456', 'marc': 'papa', 'model': 'papa II', 'year': 2010, 'paid': 'Sí'},
                                 {'plac': 'QW7E89', 'marc': 'PAPA III', 'model': 'PAPA IV', 'year': 2015, 'paid': 'Sí'}]},
          '1283728391': {'name': 'ALFONSO', 'tel': 87654321,
                         'cars': [{'plac': '101', 'marc': 'PALA', 'model': 'PALA II', 'year': 2007, 'paid': 'Sí'},
                                  {'plac': 'AWEU', 'marc': 'PALA III', 'model': 'PALA IV', 'year': 2020, 'paid': 'No'},
                                  {'plac': '9Q8EA', 'marc': 'PALA V', 'model': 'PALA VI', 'year': 2026, 'paid': 'Sí'}]}}

placas =  []
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
    print("-"*20+f"PROPIETARIO {i+1}"+"-"*20)
    while True:
        nit = input("▶  Ingrese su número de identificación (NIT): ")
        if nit in proper: print(error_mesagge)
        else: break

    name = input("▶  Ingrese su nombre completo: ")
    while True:
        tel = input_integer("▶  Ingrese su número de teléfono: ")
        if len(str(tel)) == 8: break
        else: print('-'*50+'\n'+"✖"*5+"   Lo siento, verifique que el telefono tenga 8 digitos   "+"✖"*5)

    while True:
        c_cars = input_integer("▶  Ingrese la cantidad de vehículos que posee: ")
        if c_cars>0: break
        else: print(error_mesagge)

    cars = []
    for j in range(c_cars):
        print("-"*10+f"VEHICULO {j+1}"+"-"*10)
        while True:
            plac = input("▶  Ingresa placa: ")
            if plac in placas:
                placas.pop()
                print(error_mesagge)
            else:
                placas.append(plac)
                break
        marc = input("▶  Ingresa el nombre de la marca: ")
        model = input("▶  Ingresa el modelo del auto: ")
        year = input_integer("▶  Ingresa el año del vehiculo: ")

        while True:
            print('   1) Sí\n   2) No')
            imp_pay = input_integer("▶  Usted ha pagado su impuesto?: ")
            if 1<=imp_pay<= 2: 
                if imp_pay == 1: imp_pay = 'Sí'
                elif imp_pay == 2: imp_pay = 'No'
                break
            else: print(error_mesagge)
        cars.append({'plac':plac,'marc': marc,'model': model,'year': year, 'paid': imp_pay})

    proper[nit]={
        'name': name,
        'tel': tel,
        'cars' : cars
    }

print('~'*20+"RESUMEN DE PROPIETARIOS"+'~'*20)
for nt, values in proper.items():
    print("-"*10+f"PROPIETARIO {values['name']}"+"-"*10)
    print(f"> Identificación: {nt}")
    print(f"> Teléfono: {str(values['tel'])[:4]}-{str(values['tel'])[4:]}")
    print("> Vehiculos: ")
    for cars in values['cars']:
        print(f"   -Placa: {cars['plac']}|{cars['marc']} {cars['model']}({cars['year']})|Impuesto: {cars['paid']}")

prop_search = input("\n▶  Ingresa un NIT para buscar por separado:")
if prop_search in proper:
    for nt, values in proper.items():
        if nt == prop_search:
            print("-" * 10 + f"PROPIETARIO {values['name']}" + "-" * 10)
            print(f"> Identificación: {nt}")
            print(f"> Teléfono: {str(values['tel'])[:4]}-{str(values['tel'])[4:]}")
            print("> Vehiculos: ")
            for cars in values['cars']:
                print(f"   -Placa: {cars['plac']}|{cars['marc']} {cars['model']}({cars['year']})|Impuesto: {cars['paid']}")
else: print("\nLo sentimos, no lo hemos encontrado")

paid_count = 0
no_paid_count= 0
for i in proper.values():
    for j in i['cars']:
        if j['paid'] == 'Sí': paid_count+=1
        if j['paid'] == 'No': no_paid_count+=1
print(f"\n\nTotal de impuestos pagados: {paid_count}" )
print(f"Total de impuestos no pagados: {no_paid_count}" )

