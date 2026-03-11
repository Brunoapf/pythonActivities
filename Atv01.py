nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Olá, " + nome + " " + sobrenome + "! Seja bem-vindo(a)!")

idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
else:    print("Você é maior de idade.")