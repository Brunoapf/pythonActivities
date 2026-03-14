num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num1 , num2 = int(num1), int(num2)

try:
    print(num1 / num2)
except ZeroDivisionError as error:
    print(f"Erro: {error}")

"""
try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
except ValueError:
    print("Erro: valor inválido! Digite um número.")
except ZeroDivisionError:
    print("Erro: não divida por zero!")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Fim da execução.")

"""