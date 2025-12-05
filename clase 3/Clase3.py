# operaciones
# aritmeticas
# + - * / esenciales
# **potencia , % modulo, //division entera 
# <, >, <=, >=, ==, !=  operaciones
numero = 1 #asignacion
2 == 2 # comparacion
# logicas los que me permiten analizar condiciones
# and $ , me da verdadero unicamente cuando ambas condiciones sean verdadero
# or | , me da falso unicamente cuando ambas condiciones sean falsas
# not negacion 

#mostrar informaccion en pantalla
print("clase 3")
num1 = 5
num2 = 10
respuesta = num1 + num2
print(respuesta)
#inputs me permite interactuar con la consola
nombre = input("ingrese su nombre: ")
print("hola " + nombre)

#Elaborar una calculadora de la suma de dos numeros ingresados por el usuario
numero1 = input("ingrese el primer numero: ")
numero2 = input("ingrese el segundo numero: ")
suma = float(numero1) + float(numero2)
print("la suma de los dos numeros es: " + str(suma))

"""n1 = input("Ingrese el numero 1 : ")
n1 = int(n1)
n2 = int(input("Ingrese el numero 2 : "))
print(f"la suma de los dos numeros es {n1 + n2}")"""

"""n1 = input("Ingrese el numero 1 : ")
n1 = float(n1)
n2 = float(input("Ingrese el numero 2 : "))
print(f"la suma de los dos numeros es " +str (n1 + n2))"""

#! todo lo que sea ingresado por el usuario a traves del input es considerado un string
#convertir datos
#str a int o float
"""n = "5"
print(type(n)) # type() es el tipo de dato
n = int(n) # converti a int
print(type(n))
print(n)
n = float(n)# converti a float
print(n)"""

#crear un programa que me pida el nombre apelldio y edad
#luego muestre el mensaje de bienvenida}
nombre = input("ingrese su nombre: ")
edad= input("ingrese su edad: ")
print ("Bienvenido " + nombre + " tu edad es " + edad)

#ingrese una palabra y muestre
# la palabra
# la palabra en mayusculas
# cuantas letras tiene
# una porcion de la palabra desde la segunda letra hasta la quinta

palabra = input("ingrese una palabra: ")
print(palabra)
print(palabra.upper())
print(len(palabra))
print(palabra[1:5])

# condicionales son herramientas que permiten controlas las acciones que realiza mi codigo al usuario

#if si >= if 1 o mas condiciones : si es verdadero ejecuta un bloque de codigo
#ejemplo 1
edad= 22
if edad >= 18 :
    print("eres mayor de edad")
    
#ejemnplo con and
edad= 25
dinero = True
if edad >= 18 and dinero :
    print("puedes ir al bar")

#ejemplo con or
stock_iphone= False
dinero = True
if dinero or stock_iphone :
    print("puedes comprar el iphone")
    #if else , si la condicion se cumple lo hace de lo contrario ejecuta otro bloque de codigo
#ejemplo
edad= 18
dinero = True
if edad >= 18 and dinero :
    print("puedes ir al bar")
else:
    print("no puedes ingresar al bar")


#if elif else
dinero = 5000
if dinero > 0 and dinero <= 1000 :
    print("Es pobre")
elif dinero >1000 and dinero <=3000 :
    print("Clase media")
elif dinero >3000 and dinero <=5000:
    print("Clase alta")  
else:
    print("no conozco tu situacion economica")

#anidados
edad = 14
dinero = 700

if edad >=18 :
    if dinero >400 :
        print("paga deudas")
    else: 
        print("ahorra dinero")
else:
    print("no hagas nada, estudia")