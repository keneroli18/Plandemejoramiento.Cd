# Pedimos al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Pedimos al usuario que seleccione una operación
print("Selecciona una operación:")
print("+ para sumar")
print("- para restar")
print("* para multiplicar")
print("/ para dividir")

operacion = input("Operación seleccionada: ")

# Realizamos la operación seleccionada por el usuario
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    print("Operación no válida")
    
# Mostramos el resultado al usuario
print("El resultado es:", resultado)