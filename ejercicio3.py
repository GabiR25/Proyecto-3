def funcion(promedio):
    if promedio >= 6:
        return 'APROBADO'
    else:
        return 'DESAPROBADO'
alumnos = open('ejercicio3.txt', 'w')
opc = 1
nota_final = 0

while opc != 3:
    print('\n -------------------')
    print('MENU de alumnos')
    print('-------------------')
    print(f'1. Ingresar alumno')
    print(f'2. Ver alumnos cargados')
    print(f'3. Salir')
    opc = int(input('\nIngrese la opción que usted deseé: '))

    if opc == 1:
        alumnos = open('ejercicio3.txt', 'a')
        nombre = input('Ingrese nombre y apellido del estudiante: ')
        dni = int(input('Ingrese DNI del estudiante: '))
        lista = []
        for i in range(6):
            nota = int(input(f'Ingrese la nota del TP {i + 1}º del alumno: '))
            lista.append(nota)
        
        promedio = round(sum(lista) / 6, 2)

        alumnos.write(f'\nEl alumno {nombre} de DNI: {dni}; ')
        alumnos.write(f'Se sacó las siguientes notas en los TP {lista}, en promedio su nota es {promedio} por lo que está {funcion(promedio)}')
        alumnos.close()
    elif opc == 2:
        alumnos = open('ejercicio3.txt','r')
        texto = alumnos.read()
        print(texto)
        alumnos.close()
    elif opc == 3:
        print('Gracias por utilizar el programa')
        break
    else:
        print('Opción no valida, ingrese una opción valida')

alumnos.close()