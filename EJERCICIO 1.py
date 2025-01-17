def ordenarlista(lista):
    lista.split(",")
    lista.sort()
    lista.reverse()
    file = open("listaordenada.txt", "a")
    for i in lista:
        file.write(i," ")
    file.close()
def numeropar(ficheros):
    file = open(ficheros, "r")
    lineas = file.readlines()
    print(lineas)
    numeros = []
    for i in lineas:
        numeros.append(int(i))
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    file = open("ListaPares.txt", "a")
    for i in pares:
        file.write(i,"")
        file.close()
ordenarlista(input("Dime una lista de numeros"))
numeropar(input("elije una direccion"))
