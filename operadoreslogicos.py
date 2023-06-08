# En estas dos líneas se están creando dos variables: `x` se inicializa con el valor de 5 y `y` con el valor de 10.
x = 5
y = 10
# En esta línea se está evaluando una condición utilizando los operadores lógicos `and` (y) y `<` (menor que) y `>` (mayor que). La condición se cumple si `x` es menor que 10 y `y` es mayor que 5. Si la condición se cumple, se imprime en pantalla el mensaje "Ambas condiciones se cumplen"
if x < 10 and y > 5:
  print("Ambas condiciones se cumplen")

if x < 10 or y < 5:
  print("Al menos una condición se cumple")
# En esta línea se utiliza el operador lógico `not` (no) para negar la condición. La condición original es que `x` sea mayor que `y`, pero al utilizar el operador `not`, la condición negada es que `x` no sea mayor que `y`. Como en este caso la condición negada es verdadera, se imprime en pantalla el mensaje "La condición no se cumple".
if not(x > y):
  print("La condición no se cumple")
