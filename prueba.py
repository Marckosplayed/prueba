
# Calculadora de promedios
print ("Ingrese numeros")
num1=0
num1 = int (input("ingrese numero 1: ")) 
num2=0 
num2 = int (input("ingrese numero 2: "))
num3=0
num3 = int (input("ingrese numero 3: "))
suma=num1+num2+num3
print ("El promedio es: ",suma/3)


"""
# Convertidor de dolares a euros
print ("Convertir dolares a euros")
dolar=0
dolar = int (input ("ingrese cantidad de dolares: "))
Euro = 0.93
CantidadDolar=dolar*Euro/1
print ("Tus euros serian: ",CantidadDolar)
"""


"""
# Contador de palabras
 def contar_palabras(frase):
    frase = frase.strip()
    palabras = frase.split()
    num_palabras = len(palabras)
    return num_palabras

def main():
    frase = input("Por favor, ingresa una frase: ")
    num_palabras = contar_palabras(frase)
    print("El número de palabras en la frase es:", num_palabras)

if __name__ == "__main__":
    main() 
"""


"""
# Conversor de Temperatura
print ("Eliga que temperatura quiere convertir:")
print ("Celcius --> Fahrenheit (1)")
print ("Celcius <-- Fahrenheit (2)")
valor = int(input())

celcius = 0
Fahrenheit = 0

if(valor == 1):
    celcius = int(input("Ingrese la temperatura en celcius "))
    Fahrenheit = (celcius * 9/5) + 32
    print (Fahrenheit)

if(valor == 2):
    Fahrenheit = int(input("Ingrese la temperatura en fahrenheit "))
    celcius = 5/9 *(Fahrenheit - 32)
    print (celcius)"""