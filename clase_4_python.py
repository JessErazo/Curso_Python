###### CLASE 4 ########

def saludo(nombre):
    #esta funcion saluda al nombre que ingrese
    a = print(f"Hola {nombre}!")
    return a

nombre_1 = 'Pablo'  
saludo(nombre_1) 



def calcular_promedio (numeros):
    ##esta funcion calcula una lista de numeros
    ## arg : numeros = lista de numeros
    ## returns : el primedio de la lista numeros
    suma = sum(numeros)
    promedio = suma/len(numeros)
    return promedio

lista = [1,2,3,4,5,6]
calcular_promedio (lista)


###EJEMPLO 3
import pandas as pd 
import numpy as np 

##Creamos numeros aleatorios, crear una semilla para que no se vaya cambiando constantemente
#semilla
np.random.seed(123)
#crear datos y df
regiones = np.random.choice (['A','B','C'], size=100)
ventas = np.random.randint(100, 10000, size= 100)
costos = np.random.uniform(10,500, size= 100)

df = pd.DataFrame({'region' : regiones, 'ventas': ventas, 'costos': costos})

def ventascostos_region(variable_cat):
    ##calcularemos las sumas de ventas y costos por region
    ##argumentos : variable_cat : nombre de la columna categorica del df
    ## returns : suma de las ventas y costos por region
    suma = df.groupby(variable_cat).sum()
    return suma

ventascostos_region(variable_cat= 'region')

##Version 1
def analizar_dataframe_v1(df):
    for columna in df.columns:
        if df[columna].dtype == 'float64' or df[columna].dtype == 'int':
            media = df[columna].sum()
            desviacion_estandar = df[columna].sum()
            print(f'Columna: {columna}, Media: {media}, Desviación Estándar: {desviacion_estandar}')
        else:
            conteo = df[columna].value_counts()
            print(f'Columna: {columna}, Conteo: {conteo}')


#Version 2
def analizar_dataframe_v2(df):
    for columna in df.columns:
        if df[columna].dtype in ['float64', 'int64']:
            media = df[columna].mean()
            desviacion_estandar = df[columna].std()
            print(f'Columna: {columna}, Media: {media}, Desviación Estándar: {desviacion_estandar}')
        else:
            conteo = df[columna].sum()
            print(f'Columna: {columna}, Conteo: {conteo}')


#Version 3
def analizar_dataframe_v3(df):
    for columna in df.columns:
        if df[columna].dtype in ['float64', 'int64']:
            media = df[columna].mean()
            desviacion_estandar = df[columna].std()
            print(f'Columna: {columna}, Media: {media}, Desviación Estándar: {desviacion_estandar}')
        else:
            conteo = df[columna].value_counts()
            proporcion = df[columna].value_counts(normalize=True)
            print(f'Columna: {columna}, Conteo: {conteo}, Proporción: {proporcion}')

##evaluar si la columna es numérica o categórica/texto, calcular la media y la desviación estándar
##para las columnas numéricas, y realizar el conteo y la proporción de cada categoría
##para las columnas categóricas o de texto. Además, utiliza los métodos correctos para
##realizar los cálculos estadísticos correspondientes en cada caso.            

#Version 4
def analizar_dataframe_v4(df):
    for columna in df.columns:
        if df[columna].dtype == 'object':
            media = df[columna].mean()  
            desviacion_estandar = df[columna].std()  
            print(f'Columna: {columna}, Media: {media}, Desviación Estándar: {desviacion_estandar}')
        else:
            conteo = df[columna].value_counts()
            print(f'Columna: {columna}, Conteo: {conteo}')