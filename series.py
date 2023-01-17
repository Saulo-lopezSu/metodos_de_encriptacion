import random
import numpy as np
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("SERIES")
    print(ascii_banner)
def encriptar(mensaje):
    print("1.numeros pares\n2.numeros primos\n3.numeros multiplos de 4\n")
    orden = []
    numPar = []
    numPri = []
    multiplos = [] 
    for i in range(3):
        orden.append(int(input(f'{i+1} .Orden:')))
    aux = []
    for i in orden:
        if(i==1):
            numPar = calcularNumerosPares(len(mensaje))
            aux = np.concatenate((aux,numPar))
        elif(i==2):
            numPri = calcularNumerosPrimos(len(mensaje))
            aux = np.concatenate((aux,numPri))
        elif(i==3):
            multiplos = numerosMultiplos(4,len(mensaje))
            aux = np.concatenate((aux,multiplos))
    aux = np.concatenate((aux,numerosNaturales(len(mensaje))))
    final = []
    for i in aux:
        if(i not in final):
            final.append(int(i))
        else:
            list(aux).remove(i)
    #print(f"numeros:{final}")
    encriptado = ""
    for i in final:
        encriptado = encriptado + mensaje[i]
        #print(mensaje[i],end='')
    print(f"Mensaje encriptado:{encriptado}\nOrden:{orden}")
def descifrar(mensaje, orden):
    descifrado = ""
    aux = []
    for i in orden:
        if(i==1):
            numerosPares = calcularNumerosPares(len(mensaje))
            aux = np.concatenate((aux,numerosPares))
        elif(i==2):
            numerosPrimos = calcularNumerosPrimos(len(mensaje))
            aux = np.concatenate((aux,numerosPrimos))
        elif(i==3):
            multiplos = numerosMultiplos(4,len(mensaje))
            aux = np.concatenate((aux,multiplos))

    aux = np.concatenate((aux,numerosNaturales(len(mensaje))))
    final = []
    for i in aux:
        if(i not in final):
            final.append(int(i))
        else:
            list(aux).remove(i)
    #print(final)
    contador = 0
    i=0
    while(contador < len(mensaje)):
        if(final[i] == contador):
            descifrado += mensaje[i]
            contador +=1
        else:
            if(i >= len(final)-1):
                i=0
            else:
                i+=1
    
    return descifrado
def calcularNumerosPares(cantidad):
    numeros = []
    for i in range(cantidad):
        if(i%2==0):
            numeros.append(i)
    return numeros
def calcularNumerosPrimos(cantidad):
    numeros = []
    for i in range(2,cantidad):
        contador = 2
        primo = True
        while primo and contador < i:
            if (i % contador == 0):
                primo = False
            else:
                contador += 1
        if(primo):
            numeros.append(i) 
    return numeros
def numerosNaturales(cantidad):
    numeros = []
    for i in range(cantidad):
        numeros.append(i)
    return numeros
def numerosMultiplos(multiplo, cantidad):
    numeros = []
    for i in range(cantidad):
        if(i%multiplo==0):
            numeros.append(i)
    return numeros
def numerosRandom(longitud):
    numeros = []
    for i in range(0,longitud):
        numeros.append(random.randint(0,longitud))
        unicos = list(dict.fromkeys(numeros))
    return unicos
def menu():
    print("1.Cifrar\n2.Descifrar\n3.Salir")
    opcion = int(input('Ingrese la opcion:'))
    if(opcion == 1):
        mensaje = input('ingrese el mensaje:')
        encriptar(mensaje)
    elif(opcion == 2):
        en = input('ingrese el mensaje:')
        arreglo = [int(input('orden1:')), int(input('orden2:')), int(input('orden3:'))]
        print(descifrar(en, arreglo))
    else:
        SystemExit()
banner()
print("OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion")
print("by Saulo Gonzalez L. ")
menu()
