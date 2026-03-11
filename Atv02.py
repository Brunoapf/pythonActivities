usuario = "admin"
senha = "123456"    

u = input("Digite seu usuário: ")
s = input("Digite sua senha: ") 

if u == usuario and s == senha:
    print("Login bem-sucedido! Bem-vindo, " + usuario + "!")
else:    print("Login falhou! Usuário ou senha incorretos.")