
import sys

try:
    x = int(input("Ingrese primer numero: "))
    y = int(input("Ingrese segundo numero: "))
except ValueError:
    print("Error: ingresar un valor entero")
    sys.exit(1)      # sys.exit(1): Salir del programa, 1: algo salió mal 

try:
    result = x/y
    print(f"resultado de {x} / {y} es: {result}")

except ZeroDivisionError:
    print("No s epuede dividiar entre 0.")
    sys.exit(1)