def calculadora(numero1, numero2, operador):

    if operador == "+":
        print(numero1 + numero2)

    elif operador == "-":
        print(numero1 - numero2)

    elif operador == "/":
        print(numero1 / numero2)

    elif operador == "*":
        print(numero1 * numero2)

    else:
        print("Operador inválido")


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

operador = input("Qual operação você quer (+ - / *): ")

calculadora(numero1, numero2, operador)