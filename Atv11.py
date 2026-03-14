String = "valor Qualquer"

i = 0
while i < len(String):
    letra = String[i]

    if letra == " ":
        break

    print(letra)
    i += 1
else:
    print("Fim da string")
print("Fim do programa")