# pedir al usuario ingresar un numero y me responda si el numero es mayor o menor a 10
numero = int(input("ingrese un numero: "))
if numero >= 10 :
    print("el numero es mayor a 10")
else:
    print("el numero no es mayor a 10")

#pedir un correo al usuario y verficar si termina en @gmail.com, muestre un mensaje de correo valido
correo= input("ingrese su correo: ")
if correo.endswith("@gmail.com") :
    print("correo valido")
else : 
    print ("correo no valido")

# pedir ingresar una contraseña, pedir que reingrese la contraseña y si ambas son iguales, muestre un mensaje de clave exitosa
contraseña1 = input("ingrese su contraseña: ")
contraseña2 = input("reingrese su contraseña: ")
if contraseña1 == contraseña2 :
    print("clave exitosa")
else:
    print("las contraseñas no coinciden")

