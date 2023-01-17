import pyfiglet
def banner():
    ascii_banner = pyfiglet.figlet_format("TRANSPOSICION")
    print(ascii_banner)
banner()
print("OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion")
print("by Saulo Gonzalez L. ")
def encriptar(filas, mensaje):
    matriz = []
    index =0
    encriptado = ""
    for i in range(len(mensaje)):
        matriz.append([])
        for j in range(filas):
            if (index>=len(mensaje)):
                matriz[i].append('?')
            else:
                matriz[i].append(mensaje[index])
                index = index+1

    for i in range(filas):
        for j in range(len(mensaje)):
            encriptado = encriptado+matriz[j][i]
            print(matriz[j][i],end=' ')
        print()
    print(f"filas: {filas} columnas: {len(mensaje)} mensaje encriptado: {encriptado}")
    return encriptado

def desencriptar(filas, encriptado):
    en = []
    ax = 0
    columnas = int(len(mensaje)/filas)
    for i in range(filas):
        en.append([])
        for j in range(columnas):
            en[i].append(encriptado[ax])
            ax = ax + 1

    for i in range(columnas):
        for j in range(filas):
            if(en[j][i] == '?'):
                pass
            else:
                print(en[j][i],end='')
filas = int(input("Agrega numero de filas:"))
mensaje = input('Agrega el mensaje:').upper()
encriptar(filas, mensaje)
filas = int(input('Agrega numero de filas:'))
#columnas = int(input('Numero de columnas:'))
mensaje = input('Ingrese el mensaje:').upper()
desencriptar(filas, mensaje)
print()
