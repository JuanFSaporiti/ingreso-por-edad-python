# Paso 1: Solicatar al usuario que ingrese la edad del cliente

edad = int(input("Por favor, ingrese tu edad: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingreasar al boliche. 

permitido = True if edad >= 18 else False #ternario 

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar al boliche

if permitido:
    print("Puedes entrar al boliche")
else:
    print("Lo siento mucho, nose puede ingresar al boliche siendo menor de edad")