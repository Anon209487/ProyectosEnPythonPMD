# coding: latin1  # Indicamos la codificación del archivo para soportar caracteres especiales

# main 
# -----------------------------------------------
def main():
    # Código principal del programa
    print("Hola mundo")

# Esto se asegura que el código dentro de main() se ejecute solo si este archivo 
# se ejecuta directamente (no si es importado como un módulo en otro archivo).
if __name__ == "__main__":
    main()

# imprimir datos
# -----------------------------------------------
print("Hola mundo ")
""" Declaración de variables """
x = "Esto es una variable"  # Cadena de texto
y = """Esto es otra variable"""  # Cadena de texto multilínea
numeroEntero = 5  # Número entero

# input variables 
# -----------------------------------------------
# Solicita al usuario que ingrese un número entero y lo convierte con int()
variableNumerica = int(input("Por favor, introduce un número entero: "))  
# Solicita al usuario que ingrese un texto (cadena)
variableTexto = input("Por favor, introduce un texto: ")
numero_str = "123"

# Conversiones 
# -----------------------------------------------
# Solicita al usuario que ingrese un número entero y lo convierte con int()
variableAconvertir="11"
variableAconvertir = int(variableAconvertir)
variableAconvertir = float(variableAconvertir)
variableAconvertir = str(variableAconvertir)
lista = ['H', 'o', 'l', 'a']
cadena = ''.join(lista)  # Convierte una lista de caracteres en una cadena
print(cadena)  # Salida: "Hola"
cadena = "Hola"
lista = list(cadena)  # Convierte de cadena a lista
print(lista)  # Salida: ['H', 'o', 'l', 'a']



# imprimir variables 
# -----------------------------------------------
# type() devuelve el tipo de dato de la variable x
print(type(x))  

# Multiplicación de cadenas: "Esto es una variable" se repetirá 4 veces
print(x * 4)  

# Concatenación de cadenas usando el operador +
print(x + " y " + y)  

# Imprime el substring de la cadena `y` desde el índice 2 hasta el 10 (no incluye el 10)
print(y[2:10])  

# cadenas
# -----------------------------------------------
# split() separa la cadena `x` en una lista de palabras, dividiendo por los espacios
palabras = x.split(" ")
print(palabras)

# join() une una lista de palabras con espacios, generando una nueva cadena
palabras = " ".join(['cadena', 'de', 'palabras'])
print(palabras)

# Arrays (Listas en Python)
# -----------------------------------------------
# Definición de una lista que contiene diferentes tipos de datos
lista = [22, True, "palabra", [1, 2]]

# Imprime el tercer elemento de la lista (índice 2), que es "palabra"
print(lista[2])

# Imprime el primer elemento de la lista dentro de la lista anidada (índice 3)
print(lista[3][0])

# Acceso con índices negativos, accede al penúltimo elemento de la lista
print(lista[-2])

# Recortes de listas (slicing)
listaRecortada = lista[0:4]  # Elementos desde el índice 0 hasta el 3
listaRecortada = lista[0:4:2]  # Desde el índice 0 hasta el 3, tomando uno de cada dos
listaRecortada = lista[::2]  # Toma todos los elementos de la lista, de dos en dos
listaRecortada = lista[:4]  # Desde el inicio hasta el índice 3
listaRecortada = lista[0:]  # Desde el índice 0 hasta el final

# Iteración sobre la lista
for element in lista:
    print(element)

# enumerate() devuelve el índice y el valor de cada elemento
for position, elemento in enumerate(lista):
    print(position, elemento)

# Tupla (Array inmutable en Python)
# -----------------------------------------------
# Definición de una tupla (las tuplas son inmutables, no se pueden modificar)
listaTupla = (22, 33, True, "hola")

# Recorte de la tupla (similar a listas)
listaTuplaRecortada = listaTupla[0:2]  # Primeros dos elementos de la tupla

# Bucle while para recorrer la tupla
counter = 0
while counter < len(listaTupla):
    print(listaTupla[counter])
    counter += 1

# Booleanos 
# -----------------------------------------------
condicion = 1

# Estructura condicional if-elif-else
if condicion == 1:
    print("verdadero") 
elif condicion != 1:
    print("falso") 
else:
    print("null")

# Operador ternario para asignar valores
var = "par" if (condicion % 2 == 0) else "impar"
print(var)

# Bucles
# -----------------------------------------------
edad = 0
# Bucle while que se ejecuta mientras `edad` sea menor a 18
while edad < 18:
    edad += 1
    print(edad)

# Bucle for para recorrer una cadena
cadena = input("Introduce una cadena: ")
for letra in cadena:
    print(letra)

# Bucle for con range(), imprimimos del 1 al 100 con una coma como separador
for contador in range(1, 101, 1):
    print(contador, end=",")

# Funciones
# -----------------------------------------------
# Definición de una función con parámetros por defecto
# El valor por defecto se sustituye si se indica otro valor al llamar la función
def miFuncion(param1=1, param2=4):
    """Esta función devuelve la suma de dos números"""
    res = param1 + param2
    return res

# Llamada a la función y asignación del resultado a la variable `suma`
suma = miFuncion(1, 2)
print(suma)




# clases 
class calculadora:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def suma(self):
       res=self.x + self.y 
       return res
    def resta(self):
       res=self.x - self.y
       return res
    def multiplicacion(self):
       res=self.x * self.y 
       return res
    def division(self):
        res=self.x / self.y 
        return res

from calculadora import *

variableNumericaX = int(input("Por favor, introduce un número entero: "))  
variableNumericaY = int(input("Por favor, introduce un número entero: "))  
obj = calculadora(variableNumericaX,variableNumericaY)
print("Suma: ",obj.suma())
print ("Resta: ",obj.resta())
print ("Multiplicacion: ",obj.multiplicacion())
print ("Division: ",obj.division())

# herencia clase padre y clase hija
class Padre:
    def __init__(self,nombre):
        self.nombre = nombre
    def saludo(self):
       print ("Soy la clase padre " , self.nombre)

class Hija(Padre):
    def __init__(self,nombre):
       super().__init__(nombre)

    def saludo(self):
       print ("Soy la clase hija ", self.nombre)


obj = Padre("paco")
obj2 = Hija("paca")
obj.saludo()
obj2.saludo()

#coding: latin1

def numerosEntreEnreros (param1,param2):
     for contador in range(param1,param2,1):
      print (contador , end=",")

def main():
 param1 = 0
 param2 = 0

 while param1==param2 or param1<0 or param2<0 :
    param1 = int(input("Por favor, introduce un número entero: "))
    param2 = int(input("Por favor, introduce un número entero: "))

 numerosEntreEnreros(param1, param2) 
if __name__ == "__main__":
    main()

