while True:
    print("----------- Calculadora V1.0 -----------")
    print("Menu de opções:\n [1] Multiplicar \n [2] Somar \n [3] Dividir \n [4] subtração \n [5] Sair ")
    print("-="*20)
    escolha = input("Digite sua escolha: ")
    print("-="*20)
    try:
        escolha_int = int(escolha)
        if escolha_int >= 6:
            print("ERRO! Digite a penas as escolhas de 1 a 5")
            continue
        if escolha_int == 5:
            print("Ate mais ...")
            break
        try: 
            num1 = input("Digite o primeiro numero: ")
            num2 = input("Digite o segundo numero: ")
            
            num1_int = int(num1)
            num2_int = int(num2)
            print("-="*20)   
            if escolha_int == 1:
                multipliçao = num1_int * num2_int
                print(f"O resultado da multiplicão é: {multipliçao}")
 
            if escolha_int == 2:
                soma = num1_int + num2_int
                print(f"O resultado da soma é: {soma}")
 
            if escolha_int == 3:
                divisao = num1_int / num2_int
                print(f"O resultado da divisao é:  {divisao}")
            if escolha_int == 4:
                subtraçao = num1_int - num2_int
                print(f"O resultado da subtração é {subtraçao}")
            print("-="*20)
        except:
            print("Um ou ambos os numeros estao incorretos!")
 
    except:
        print("Não existe essa escolha tente novamente!")
        continue