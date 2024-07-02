# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
seleccion = []
alergia = []

print(' Antes de iniciar, necesitamos saber un par de cosas de usted.')
name = input('¿Cuál es su nombre?: ')
com_fav = input('¿Tiene alguna comida favorita?: ')
alergias = str(input('¿Tiene alguna alergia?: '))
alergia.append(alergias)
    
# user.append({'Usuario':name,
#              'C. Fav':com_fav,
#              'Alergias':alergias})
#menu principal
while (True):
    
    print('''
          ¡Bienvenido/a al Restaurante! Porfavor, seleccione la opción que más le guste.

          [1] Menú
          [2] Selección
          [3] Pagar
          [9] Salir
                    ''')
    
    opcion = int(input('>>> '))

    if opcion == 1:
        print(var)
        while True:
            print('¿Desea seleccionar algo del menú? S/N')
            pedir = input('>>> ').lower()

            if pedir == 's':
                sel = int(input('Eliga el número del alimento: '))
                seleccion.append(var[sel-1])
                break
            if pedir == 'n':
                break

    if opcion == 2:
        print(seleccion)
        while True:
            print('¿Desea quitar algo del carrito? S/N/T (T es para limpiar el carrito)')
            car_quitar = input('>>> ').lower()
            if car_quitar == 's':
                quitar = int(input('¿Cuál item desea quitar? >>> '))
                seleccion.pop(quitar-1)
                break
            if car_quitar == 't':
                seleccion.clear()
                break
            if car_quitar == 'n':
                break
    if opcion == 3:
        total = 0
        for i in seleccion:
            seleccion['precio'] += total
            print(total)
    #esto es la cuenta

    if opcion == 9:
        print('¡Gracias por preferirnos!')
        break

    #escribir menu con funciones aqui


