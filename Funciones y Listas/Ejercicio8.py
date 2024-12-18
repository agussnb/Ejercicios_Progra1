# Crear una función para cada opción de menú
#Funcion para 1-Importar listas
#Funcion para 2-Listar los datos de los usuarios de México
#Funcion para 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
#Funcion para 4-Listar los datos del/los usuario/s más joven/es
#Funcion para 5-Obtener un promedio de edad de los usuarios
#Funcion para 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
#Funcion para 7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
#Funcion para 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
from listas_personas import *
def importar_listas():
    from listas_personas import Nombres,Edades,Paises,CodigoPostal,Mails,Telefonos
def listar_datos_mex():
    usuarios_mex = []
    for i in range(len(Paises)):
        if Paises[i] == "Mexico":
            usuario = {
                "nombre": Nombres[i],
                "edad": Edades[i],
                'pais': Paises[i],
                'codigo postal': CodigoPostal[i],
                'mail': Mails[i],
                'telefono': Telefonos[i]
            }
            usuarios_mex.append(usuario)
    for usuario in usuarios_mex:
        print(f"Datos del usuario: {usuario}")
def listar_datos_br():
    usuarios_br = []
    for i in range(len(Paises)):
        if Paises[i] == "Brasil":
            usuario = {
                "nombre": Nombres[i],
                "edad": Edades[i],
                'pais': Paises[i],
                'codigo postal': CodigoPostal[i],
                'mail': Mails[i],
                'telefono': Telefonos[i]
            }
            usuarios_br.append(usuario)
    for usuario in usuarios_br:
         print(f"Nombre: {usuario['nombre']}, Mail: {usuario['mail']}, Telefono: {usuario['telefono']}")
def listar_datos_users_jovenes():
    min_edad = min(Edades)
    menores = []
    for i in range(len(Edades)):
        if Edades[i] == min_edad:
            menores.append(i)
    for pos in menores:
        print("Los usuarios mas jovenes son: ",Nombres[pos])
def listar_promedio_edad_users():
    suma_edades = 0
    for edad in Edades:
        suma_edades += edad
    promedio = suma_edades / len(Edades)
    return promedio
def listar_br_user_max_age():
    max_edad = max(Edades)
    mayores = []
    for i in range(len(Edades)):
        if Edades[i] == max_edad and Paises[i] == "Brasil":
            mayores.append(i)
    for pos in mayores:
        print('Los usuarios Brasileros mayores son : ',Nombres[pos])
def listar_br_mex_cp():
    usuarios = []
    for i in range(len(Paises)):
        if Paises[i] == "Brasil" or Paises[i] == "Mexico":
            if CodigoPostal[i] > 8000:
                usuario = {
                "nombre": Nombres[i],
                "edad": Edades[i],
                'pais': Paises[i],
                'codigo postal': CodigoPostal[i],
                'mail': Mails[i],
                'telefono': Telefonos[i]
            }
            usuarios.append(usuario)
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, País: {usuario['pais']}, "
              f"Código Postal: {usuario['codigo postal']}, Email: {usuario['mail']}, "
              f"Teléfono: {usuario['telefono']}")
            
def listar_ita_users_mayores_cuarenta():
    usuarios = []
    
    for i in range(len(Paises)):
        if Paises[i] == "Italia" and Edades[i] > 40:
            usuario = {
                "nombre": Nombres[i],
                "mail": Mails[i],
                "telefono": Telefonos[i]
            }
            usuarios.append(usuario)
    
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, "
              f"Email: {usuario['mail']}, "
              f"Teléfono: {usuario['telefono']}")

