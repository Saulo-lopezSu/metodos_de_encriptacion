print("""
 _____ ____  ___ _____ _   _ _____ __  __ ___ _   _ ____  
|_   _|  _ \|_ _|_   _| | | | ____|  \/  |_ _| | | / ___| 
  | | | |_) || |  | | | |_| |  _| | |\/| || || | | \___ \ 
  | | |  _ < | |  | | |  _  | |___| |  | || || |_| |___) |
  |_| |_| \_\___| |_| |_| |_|_____|_|  |_|___|\___/|____/ 
                                                          
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
        clave = clave + 1
    return encriptado
def descifrar(mensaje, clave):
    desencriptado = ''
    for letra in mensaje:
        resultado = alfabeto.find(letra) - clave
        modulo = int(resultado) % len(alfabeto)
        desencriptado = desencriptado + str(alfabeto[modulo])
        clave = clave + 1
    return desencriptado
mensaje = input('Agrega texto a cifrar:').upper()
clave  = int(input('Agrega una clave:'))
print(cifrar(mensaje,clave))
mensa = input('Agrega el texto cifrado:').upper()
clave  = int(input('Agrega la clave:'))
print(descifrar(mensa,clave))
