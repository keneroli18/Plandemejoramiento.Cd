num1 = int(input("digite un numero: "))
num2 = int(input("digite otro numero: "))

if num1%2==0 and num2%2==0:
    print("ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print(f"{num1} y {num2} no son pares")
    
