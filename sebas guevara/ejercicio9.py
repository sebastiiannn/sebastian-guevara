num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")
else:
    print("No se puede dividir entre cero.")
