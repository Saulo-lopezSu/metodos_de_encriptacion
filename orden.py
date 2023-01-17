import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("ORDEN")
    print(ascii_banner)
banner()
print("OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion)
print("by Saulo Gonzalez L. ")

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789_"
clave = "rcipto".upper()
def encriptar(filas, mensaje, clave):
    print(len(mensaje))
    posiciones = []
    orden = []
    matriz = []
    index =0
    encriptado = ""
    for i in range(len(clave)):
        orden.append(0)

    for i in range (len(clave)):
        posiciones.append(alfabeto.find(clave[i]))
        # print(f"pos:{i}, c:{clave[i]}", end=' ')

    print(posiciones)

    for i in range(len(posiciones)):
        maximo = max(posiciones)
        if( i== 0):
            orden[len(clave)-1]=(posiciones.index(maximo))
        else :
            minimo = min(posiciones)
            orden[i-1]=(posiciones.index(minimo))
            posiciones[posiciones.index(minimo)] = maximo

    for i in range(len(mensaje)):
        matriz.append([])
        for j in range(len(clave)):
            if (index>=len(mensaje)):
                matriz[i].append('X')
            else:
                matriz[i].append(mensaje[index])
                index = index+1

    for i in range(filas):
        for j in range(len(clave)):
            #encriptado = encriptado+matriz[i][j]
            print(matriz[i][j],end=' ')
        print()
    
    for i in orden:
        for j in range(filas):
            encriptado = encriptado+matriz[j][i]

    print(f"filas: {filas} columnas: {len(mensaje)} mensaje encriptado: {encriptado}")
    return encriptado

def descifrar(filas, mensaje, clave):
    print(len(mensaje))
    orden = []
    posiciones = []
    posicionesaux = []
    matriz = []
    nuevaClave = ''
    descifrado = ''
    index = 0
    for i in range(len(clave)):
        orden.append(0)
    for i in range (len(clave)):
        posiciones.append(alfabeto.find(clave[i]))
        posicionesaux.append(alfabeto.find(clave[i]))
    posicionesaux.sort()
    for i in posicionesaux:
        nuevaClave = nuevaClave + alfabeto[i]
        print(alfabeto[i],end='')
    for i in range(len(clave)):
        orden[i] = nuevaClave.find(clave[i])
        #print(clave.find(nuevaClave[i]),end='')
    print(orden)
    for i in range(len(clave)):
        matriz.append([])
        for j in range(filas):
            if (index>=len(mensaje)):
                matriz[i].append('X')
            else:
                matriz[i].append(mensaje[index])
                index = index+1

    for i in range(filas):
        for j in range(len(clave)):
            print(matriz[j][i],end=' ')
        print()
    for i in range(filas):
        for j in orden:
            descifrado = descifrado+matriz[j][i]
    print(descifrado)
encriptar(4,"la clave secreta".upper(),clave)
descifrar(4,"AEEX  TXACXXCSAXLVRXLEXX".upper(),clave)
