def loops():
    try:
        usuario = int(input("Digite um número: "))

        if usuario < 0:
            print("Digite um número positivo!")
            return

        contador = 0

        while contador < usuario:
            contador += 1
            print(f"Contador: {contador}")

    except ValueError:
        print("Digite apenas números!")

def main():
    loops()

if __name__ == "__main__":
    main()