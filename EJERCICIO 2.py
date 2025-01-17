diccionario = {}
while True: 
    seleccionar = int(input('Eliga:\n''1-Añade un alumno\n''2-Mostrar Nº aprobados\n''3-Mostrar alumnado\n'))
    if seleccionar == 1:
        alumno = input('Nombre del alumno: ')
        aprobado = bool(int(input(' 0 si suspende '' 1 si ha aprobado: \n')))
        diccionario[alumno] = aprobado

    elif seleccionar == 2:
        aprobados = 0
        for aprobado in diccionario.values():
            if aprobado:
                aprobados += 1
        print('Nº Aprobados: ' + str(aprobados)+'\n')
    elif seleccionar == 3:
        print(diccionario.keys())
    else:
        print('Opción inexistente\n')