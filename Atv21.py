listaDeCompras = []

def adicionarItens():
    while True:
        item = input("Digite o nome do item que deseja adicionar (ou 'sair' para finalizar): ")
        if item.lower() == 'sair':
            break
        listaDeCompras.append(item)
        print(f"'{item}' adicionado à lista de compras.")
        continue
def exibirLista():
    print("\nLista de Compras:")
    for index, item in enumerate(listaDeCompras, start=1):
        print(f"{index}. {item}")
def apagarItem():
    while True:
        exibirLista()
        apagarItem = input("O que deseja apagar da lista? (ou 'sair')")
        if apagarItem.lower() == "sair":
            break
        try:listaDeCompras.remove(apagarItem)
        except ValueError:
            print(f"'{apagarItem}' não encontrado na lista de compras.")
        else:
            print(f"'{apagarItem}' removido da lista de compras.")
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar itens à lista de compras")
        print("2. Exibir lista de compras")
        print("3. Apagar item da lista de compras")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionarItens()
        elif escolha == '2':
            exibirLista()
        elif escolha == '3':
            apagarItem()
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
