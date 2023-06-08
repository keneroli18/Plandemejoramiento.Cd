# Definimos el saldo inicial de la cuenta
saldo = 1000

# Pedimos al usuario que ingrese su número de PIN
pin = input("Ingrese su número de PIN: ")

# Verificamos si el PIN es correcto
if pin == "1234":
    # Si el PIN es correcto, pedimos al usuario que seleccione una opción
    print("Bienvenido al cajero automático")
    print("Seleccione una opción:")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    
    opcion = int(input("Opción seleccionada: "))
    
    # Si el usuario selecciona la opción 1, mostramos el saldo actual
    if opcion == 1:
        print("Su saldo actual es:", saldo)
        
    # Si el usuario selecciona la opción 2, pedimos el monto a retirar y verificamos si hay suficiente saldo
    elif opcion == 2:
        monto = int(input("Ingrese el monto a retirar: "))
        
        if monto > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= monto
            print("Retire su dinero. Su saldo actual es:", saldo)
            
    # Si el usuario selecciona una opción no válida, mostramos un mensaje de error
    else:
        print("Opción no válida")
        
else:
    # Si el PIN es incorrecto, mostramos un mensaje de error
    print("PIN incorrecto")