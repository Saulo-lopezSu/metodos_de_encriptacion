
print("""
 ___ ___    _____  __ _   _ __
/ __|/ _ \ / ___/ / _` | | '__/
 (__|  __/ (__  )| (_| | | | 
\___|\___|/____/  \__,_| |_|
 OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion
 by Saulo Gonzalez L. 
    """)

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789 '
def cifrar(mensaje, clave):
    encriptado = ''
    for letra in mensaje:
        resultado = alfabeto.find(letra) + clave
        modulo = int(resultado) % len(alfabeto)
        encriptado = encriptado + str(alfabeto[modulo])
    return encriptado
def descifrar(mensaje, clave):
    desencriptado = ''
    for letra in mensaje:
        resultado = alfabeto.find(letra) - clave
        modulo = int(resultado) % len(alfabeto)
        desencriptado = desencriptado + str(alfabeto[modulo])
    return desencriptado
mensaje = input('Ingrese el mensjae:').upper()
clave  = int(input('Ingrese la clave:'))
print(cifrar(mensaje,clave))
mensa = input('Ingrese el mensjae:').upper()
print(descifrar(mensa,clave))
