#Interpolação de string
nome = "Bruno"
preco = 200.99041

variavel = "%s, o preço do produto é R$ %.i" % (nome, preco)
print(variavel)



print("o Hexadecimal de %d é %05x" % (255, 255))