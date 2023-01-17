

print("""
    _______  _______  ___      __   __  _______  ___   _______  _______ 
   |       ||       ||   |    |  | |  ||  _    ||   | |       ||       |
   |    _  ||   _   ||   |    |  |_|  || |_|   ||   | |   _   ||  _____|
   |   |_| ||  | |  ||   |    |       ||       ||   | |  | |  || |_____ 
   |    ___||  |_|  ||   |___ |_     _||  _   | |   | |  |_|  ||_____  |
   |   |    |       ||       |  |   |  | |_|   ||   | |       | _____| |
   |___|    |_______||_______|  |___|  |_______||___| |_______||_______|
 OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion
 by Saulo Gonzalez L. 
    """)

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789 '
def encriptar(mensaje, columnas):
    filas = len(mensaje)
    matriz = crearMatriz(filas, columnas)
    print()
    for i in range(filas):
        for j in range(filas):
            for k in range(columnas):
                if(matriz[j][k]==mensaje[i]):
                    print(f"{j}{k}",end='')
    print()
def desencriptar(mensaje, columnas):
    longitud = len(mensaje)/2
    matriz = crearMatriz(int(longitud),columnas)
    for i in range(0,len(mensaje),2):
        print(matriz[int(mensaje[i])][int(mensaje[i+1])],end='')
    print()
def crearMatriz(filas, columnas):
    indice = 0
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            if (indice > 36):
                matriz[i].append('*')
            else:
                matriz[i].append(alfabeto[indice])
                indice = indice + 1
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j],end= ' ')
        print()
    print()
    return matriz
mensaje = input('Agrega el texto a cifrar:').upper()
columnas  = int(input('Agrega el numero de filas:'))
encriptar(mensaje,columnas)
mensaje = input('Agrega el texto cifrado:')
column  = int(input('Agrega el numero de filas:'))
if column==columnas:
    desencriptar(mensaje,column)
else:
    print("clave incorrecta :c\n")
    mensaje = input('Agrega el texto cifrado:')
    column  = int(input('Agrega el numero de filas:'))
    desencriptar(mensaje,column)
