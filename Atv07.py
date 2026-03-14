"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def number():
    try:
        num = int(input("Digite um número inteiro: "))
        if num % 2 == 0:
            print(f"O número {num} é par.")
        else:
            print(f"O número {num} é ímpar.")
    except ValueError:
        print("Isso não é um número inteiro.")
number()

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora atual (0-23): ")

if hora.isdigit():
    hora = int(hora)
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24:
        print("Boa noite!")
    else:
        print("Hora inválida. Por favor, digite um número entre 0 e 23.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


