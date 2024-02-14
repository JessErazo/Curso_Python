###### Recordatorio Funciones #####################

def saludo(nombre):
    #esta funcion nos saluda cuando damos nuestro nombre
    #nombre: "una lista con mi nombre"
    #return: un saludo con el nombre dado
    print(f"Hola {nombre}")

yo = "Jess"

saludo(yo)

def suma_resta(a=3,b=7):
    x = a+b-3*b
    return(x)

y = suma_resta(a,b)
print(y)