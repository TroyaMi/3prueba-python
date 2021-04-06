"""
crear un programa que le pida al usuario su edad, nombre, dos números y muestre por pantalla:
    - suma
    - resta
    - multiplicación
    - o división (dependiendo de la opcion)
    - de ambos números seguidos de su nombre y edad
    NOTA: si el usuario no es mayor de 5 años, no puede usar el programa
"""

edad = int(input("Digite su edad: "))
if edad < 5:
    print("\n""No le esta permitido usar el programa")

Nombr = str(input("\n""Digite su nombre: "))
    
num1 = int(input("\n""Digite primer numero: "))
num2 = int(input("\n""Digite segundo numero: "))

print("\n""¿Que operacion desea realizar?")
n = int(input("1. Suma \n2. Resta \n3. Multiplicacion \n4. Divicion : \n"))

if n==1 :
    resultado = num1 + num2 
    print("\n""Resultado",resultado  ,"\n""Edad: " ,edad , "\n""Nombre: ",Nombr)

elif n==2: 
    rest = num1 - num2 
    print("\n""Resultado",rest  ,"\nEdad: " ,edad , "\n""Nombre: ",Nombr)

elif n==3:
    mult = num1 * num2
    print("\n""Resultado",mult  ,"\nEdad: " ,edad, "\n""Nombre: ",Nombr )

elif n==4:
    divi = num1 / num2
    print("\n""Resultado",divi  ,"\nEdad: " , edad , "\n""Nombre: ",Nombr)


          

        









