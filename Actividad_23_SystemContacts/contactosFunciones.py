#Esteban Elias Pacheco Vega
"""
Crea un programa en Python que gestione una lista de contactos
"""
from tabulate import tabulate
import os
import msvcrt
import time
import csv
import re 

#Colecciones para almacenar contactos
CONTACTOS = []

def limpiar():
    print('<<Press any key to continue>>')
    msvcrt.getch()
    os.system('cls')

def espera():
    time.sleep(1)   #Añade un retraso de 1 segundo

def printR(texto):  #Color rojo
    print(f'\033[31m{texto}\033[0m')

def printA(texto):  #Color Verde
    print(f'\033[32m{texto}\033[0m')

def printV(texto):  #Color Amarillo
    print(f'\033[33m{texto}\033[0m')

#Interfaz inicio
def menu():
    printA('\nSistema gestión de Contactos 📱👥')
    printA('-------------------------------------------')
    print("""1) Agregar un contacto.
2) Mostrar contactos.
3) Guardar contactos en un archivo CSV.
4) Salir del programa.""")
    printA('-------------------------------------------')  

def validarTelefono(numero):
    #Validación formato de número de teléfono
    return re.match(r'^\+?[\d\s-]{5,}$', numero) is not None #Al menos 5 caracteres para permitir códigos de país largos

def validarEmail(email):
    #Validación de formato de correo electrónico
    return re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email) is not None

def telefonoDuplicado(telefono):
    #Verificar si el número de teléfono ya está en la lista de contactos
    for contacto in CONTACTOS:
        if contacto[1] == telefono:
            return True
    return False

def emailDuplicado(email):
    #Verificar si el correo electrónico ya está en la lista de contactos
    for contacto in CONTACTOS:
        if contacto[2] == email:
            return True
    return False    

def validarNombre(nombre):
    #Verificar si el nombre no está vacío, no contiene solo espacios y que tenga al menos 3 caracteres
    return bool(nombre.strip() and len(nombre.strip()) >= 3)

#Registramos contacto
def agregarContacto():
    #Ingresamos nombre del contacto
    while True:
        nombre = input('Ingrese el nombre del contacto: ').strip().title()
        if validarNombre(nombre):
            break
        else:
            printR('El nombre no puede estar vacío, contener solo espacios o tener menos de 3 caracteres. Por favor, ingrese un nombre válido.')

    #Validación del número de teléfono
    while True:
        telefono = input('Ingrese el número de teléfono del contacto (puede incluir código de país, espacios o guiones): ').strip()
        if not validarTelefono(telefono):
            printR('Número de teléfono no válido. Debe contener solo dígitos, espacios, guiones y opcionalmente un prefijo "+" para el código de país.')
        elif telefonoDuplicado(telefono):
            printR('Número de teléfono duplicado. Por favor, ingrese un número diferente.')
        else:
            break

    #Validación del correo electrónico
    while True:
        email = input('Ingrese el correo electrónico del contacto: ').strip().lower()
        if not validarEmail(email):
            printR('Correo electrónico no válido. Formato esperado: ejemplo@dominio.com')
        elif emailDuplicado(email):
            printR('Correo electrónico duplicado. Por favor, ingrese un correo diferente.')
        else:
            break
    #Agregamos contacto a la coleccion
    CONTACTOS.append([nombre, telefono, email])
    printA(f'El Contacto "{nombre}" ha sido agregado a contactos.')

#Mostrar los contactos que hay en el sistema
def mostrarContactos():
    if len(CONTACTOS) > 0:
        headers = ['#', 'Nombre', 'Teléfono', 'Email']
        contactos_lista = [[idx + 1, c[0], c[1], c[2]] for idx, c in enumerate(CONTACTOS)] 
        print(tabulate(contactos_lista, headers=headers, tablefmt='grid'))
    else:
        printR('No hay contactos registrados.')

#Guardamos los contactos en un archivo csv
def guardarContactosCSV():
    if len(CONTACTOS) > 0:
        nombre_archivo = input('Ingrese el nombre del archivo (sin extensión): ')
        with open(f'{nombre_archivo}.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',')
            CONTACTOS.insert(0,['Nombre', 'Teléfono', 'Email']) #ENCABEZADO
            writer.writerows(CONTACTOS)
            CONTACTOS.pop(0)
        printA(f'Contactos guardados en {nombre_archivo} exitosamente.')
    else:
        printR('No hay contactos registrados.')

def main():

    while True:
        limpiar()
        menu()
        opcion = input('Seleccione: ')

        if opcion == '4':
            print("Saliendo del programa...")
            espera()
            break
        elif opcion == '1':
            printV('Registrar Contacto')
            agregarContacto()
        elif opcion == '2':
            printV('Mostrar Contactos')
            mostrarContactos()
        elif opcion == '3':
            printV('Guardar contactos en un archivo CSV')
            guardarContactosCSV()
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
