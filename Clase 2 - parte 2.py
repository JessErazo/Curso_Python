#variable de texto
mi_variable = "Hola mundo"
print(mi_variable)

#lista de números

mi_lista = [1,2,3,4,5]
print(mi_lista)

#Diccionario 
mi_diccionario = {"clave_1" : "valor1", "clave_2": "valor2", "clave_3":"valor3"}
print(mi_diccionario)

#Tipos de variables

#Numerica
vector_enteros = [10]*5
print(vector_enteros)

vector_flotantes = [3.14]*5
print(vector_flotantes)


diccionario = {"entero": vector_enteros, "flotante": vector_flotantes}
print(diccionario)

#Cadenas (salidas de mensajes "texto", identificadores, etiquetas)

cadena_simple = 'Hola mundo'
cadena_doble = ["Python es poderoso", "Me gusta mucho"]
print(cadena_doble)

###########################################
#Dataframe

import pandas as pd
# Crear un DataFrame con los datos de rendimiento en juegos
datos = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'Juego 1 (puntos)': [150, 180, 130, 200],
    'Juego 2 (puntos)': [120, 90, 110, 150],
    'Juego 3 (puntos)': [200, 160, 180, 190]
}
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)






