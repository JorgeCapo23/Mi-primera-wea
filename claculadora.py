def menu_de_entrada():
    print("Bienvenido")
    print("estas son las operaciones que puedes hacer:")
    print("1-Suma")
    print("2-Resta")
    print("3_Multiplicacion")
    print("4-Division")
print(menu_de_entrada())
numero_de_menu = int(input("ingresa un numero"))


while numero_de_menu == 1:
    print("usted esta haciendo una suma")
    numero1 = int(input("primer numero"))
    numero2 = int(input("segundo numero"))
    print("el resultado de la sumas es:"+ str(numero1 + numero2))
    numero_de_decision = int(input("quiere hacer otra suma? 1-si/2-no"))
    if numero_de_decision == 2:
        numero_de_menu = 0

print(menu_de_entrada())
numero_de_menu = int(input("ingresa un numero"))
while numero_de_menu == 2:
    print("usted esta haciendo una resta")
    numero1 = int(input("primer numero"))
    numero2 = int(input("segundo numero"))
    print("el resultado de la resta es:"+ str(numero1 - numero2))
    numero_de_decision = int(input("quiere hacer otra resta? 1-si/2-no"))
    if numero_de_decision == 2:
        numero_de_menu = 0
print(menu_de_entrada())
numero_de_menu = int(input("ingresa un numero"))

