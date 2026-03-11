usuario = "admin"
senha = "123456"    

u = input("Digite seu usuário: ")
s = input("Digite sua senha: ") 

if u == usuario and s == senha:
    print("Login bem-sucedido! Bem-vindo, " + usuario + "!")
else:    print("Login falhou! Usuário ou senha incorretos.")

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )