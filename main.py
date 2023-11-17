import secrets
import string
import time
import os
import platform

#limpia la pantalla
def clearScrean():
    time.sleep(1.5)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Genera las contraseñas
def pwsgenerator(large):
    characters = string.ascii_letters + string.digits + string.punctuation

    pws = ''.join(secrets.choice(characters) for char in range(large))

    return pws

# Guarda las contraseñas en un archivo .txt
def savepsw(archivo, contraseñas_generadas):
    with open(archivo, 'a+') as file:
        file.write('\n---------------\n')
        for i, pws in enumerate(contraseñas_generadas, start=1):
            file.write(f'{i} ====> {pws}\n')
os.system('cls')
# Pide el numero de contraseñas hasta que introduzca un valor valido (entero)
while True:

    num_pws = input('Ingrese el numero de contraseñas a generar: ')
    if num_pws.isdigit():
        num_pws = int(num_pws)

        if num_pws <= 0:
            print('El numero de contraseñas a generar debe ser mayor a 0')
            clearScrean()
            continue

        else:
            clearScrean()
            break
    else:
        print('No se permiten letras o caracteres especiales')
        clearScrean()
        continue

# Pide el largo de la contraseña hasta que introduzca un valor valido (entero)
while True:

    large = input('Ingrese el largo de la/s contreseña/s a generar: ')
    if large.isdigit():
        large = int(large)

        if large < 12:
            print('El largo de tu contraseña debe ser minimo de 12 caracteres')
            clearScrean()
            continue

        else:
            clearScrean()
            break
    else:
        print('No se permiten letras o caracteres especiales')
        clearScrean()
        continue

# Pide que se introduzca un valor hasta que sea S o N

confirmacion = input('Quieres guardar tus contraseñas en un archivo .txt? (S | N): ').upper()
os.system('cls')

while confirmacion != "S" and confirmacion != "N":
    confirmacion = input('Quieres guardar tus contraseñas en un archivo .txt? (S | N): ').upper()
    clearScrean()

# Si respondio 'S' pedira el nombre del archivo hasta que los ultimos 4 caracteres sean .txt
if confirmacion == "S":
    nom_archivo = input('Ingrese el nombre en donde quiere guardar su/s contraseña/s\nSi no existe se creara'
                        'el archivo, y si existe se unira a este.\n**El archivo debe terminar en ".txt"**:  ')
    clearScrean()
    while nom_archivo[-4:] != ".txt":
        nom_archivo = input('Ingrese el nombre en donde quiere guardar su/s contraseña/s\nSi no existe se creara'
                            'el archivo, y si existe se unira a este.\n**El archivo debe terminar en ".txt"**:  ')
        clearScrean()

# Se generan las contraseñas
contraseñas_generadas = [pwsgenerator(large) for i in range(num_pws)]
print('solo tendras 30 segs para copiar tus contraseñas en fisico, de otra manera desapareceran\n!!Se rapido¡¡')
clearScrean()

#Se imprimen en pantalla con un limite de tiempo
print('Contraseñas generadas: ')
for i, pws in enumerate(contraseñas_generadas, start=1):
    print(f"{i} : {pws}")

for x in range(30, 0, -1):
    print(f'Tan solo te quedan {x} segs para copiar tus contraseñas', end='\r')
    time.sleep(1)
os.system('cls')

# Si respondio a que si quiere guardar en un archivo, guardara las contraseñas en el nombre
# del archivo que indrucio antes
if confirmacion == 'S':
    savepsw(nom_archivo, contraseñas_generadas)
    print('Tus contraseñas han sido guardadas en el archivo ===> {}'.format(nom_archivo))
    clearScrean()

for x in range(5,0,-1):
    print(f'El programa se cerrara en {x}', end="\r")
    time.sleep(1)
