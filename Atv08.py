num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num1 , num2 = int(num1), int(num2)

try:
    print(num1 / num2)
except ZeroDivisionError as error:
    print(f"Erro: {error}")

