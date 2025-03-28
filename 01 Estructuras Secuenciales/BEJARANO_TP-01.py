# Punto numero 1
print("Este programa imprime 'Hola mundo' en pantalla.")
print("Hola mundo")

# Punto numero 2
print("Este programa solicita al usuario su nombre y luego lo saluda.")
print("ingrese su nombre: ")
nombre = input()


# print("Hola", nombre, "!")
# Corrección: con el consejo del profe
print(f"Hola {nombre}!")

# Punto numero 3
print("Este programa solicita al usuario su nombre, apellido, edad y lugar de residencia, y luego muestra esa información.")
print("Ingrese su nombre: ")
nombre = input()
print("Ingrese su apellido: ")
apellido = input()
print("Ingrese su edad: ")
edad = input()
print("Ingrese su lugar de Residencia: ")
lugar = input()
print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# Punto numero 4
print("Este programa calcula el área y el perímetro de un círculo dado su radio.")
print("Ingrese el radio de un circulo: ")
radio = float(input())
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

# Punto numero 5
print("Este programa convierte una cantidad de segundos ingresada por el usuario a horas.")
print("Ingrese una cantidad de segundos: ")
segundos = int(input())
horas = segundos // 3600
print(f"Su tiempo en segundos es {segundos} y en horas es {horas}")

# Punto numero 6
print("Este programa muestra la tabla de multiplicar del número ingresado por el usuario.")
print("Ingrese un numero: ")
numero1 = int(input())
print(f"La tabla de multiplicar de su numero es: ")
print(f"{numero1} x 1 = {numero1 * 1}")
print(f"{numero1} x 2 = {numero1 * 2}")
print(f"{numero1} x 3 = {numero1 * 3}")
print(f"{numero1} x 4 = {numero1 * 4}")
print(f"{numero1} x 5 = {numero1 * 5}")
print(f"{numero1} x 6 = {numero1 * 6}")
print(f"{numero1} x 7 = {numero1 * 7}")
print(f"{numero1} x 8 = {numero1 * 8}")
print(f"{numero1} x 9 = {numero1 * 9}")
print(f"{numero1} x 10 = {numero1 * 10}")

# Punto numero 7
print("Este programa realiza operaciones matemáticas básicas (suma, resta, multiplicación y división) entre dos números ingresados por el usuario.")
print("Ingrese un numero: ")
numeroPun7_2 = int(input())
print("Ingrese otro numero: ")
numeroPun7_3 = int(input())
print(f"La suma de los numeros ingresados es: {numeroPun7_2 + numeroPun7_3}")
print(f"La resta de los numeros ingresados es: {numeroPun7_2 - numeroPun7_3}")
print(
    f"La multiplicacion de los numeros ingresados es: {numeroPun7_2 * numeroPun7_3}")
print(
    f"La division de los numeros ingresados es: {numeroPun7_2 / numeroPun7_3}")

# Punto numero 8
print("Este programa calcula el índice de masa corporal (IMC) del usuario a partir de su peso y altura.")
print("Ingrese su peso en kg: ")
peso = float(input())
print("Ingrese su altura en metros: ")
altura = float(input())
imc = peso / altura ** 2
print(f"Su indice de masa corporal es: {imc}")

# Punto numero 9
print("Este programa convierte una temperatura ingresada en grados Celsius a grados Fahrenheit.")
print("Ingrese su temperatura en grados Celsius: ")
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Punto numero 10
print("Este programa calcula el promedio de tres números ingresados por el usuario.")
print("Ingrese un primer numero: ")
numero1 = int(input())
print("Ingrese un segundo numero: ")
numero2 = int(input())
print("Ingrese un tercer numero: ")
numero3 = int(input())
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los numeros ingresados es: {promedio}")

# Bejarano Matías Osvaldo
# Cambio para Git