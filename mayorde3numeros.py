#con estas variables podemos agregar o digitar cualquier numero
num1 = int(input("digite un numero: "))
num2 = int(input("digite un numero: "))
num3 = int(input("digite un numero: "))

if num1>=num2 and num1>=num3:
    print(f"el numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"el numero mayor es {num3}")
