# ==========================================================
# SISTEMA DE ESTOQUE SIMPLES
# ==========================================================
# Este sistema permite:
# - Cadastrar produtos
# - Listar produtos
# - Atualizar quantidade
# - Remover produto
# - Sair do sistema
#
# Tudo usando conceitos básicos de lógica.
# ==========================================================


# Lista que armazenará os produtos
# Cada produto será um dicionário
estoque = []


# ----------------------------------------------------------
# Função para cadastrar produto
# ----------------------------------------------------------
def cadastrar_produto():
    print("\n=== Cadastro de Produto ===")

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    # Criando um dicionário com os dados do produto
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adicionando o produto na lista estoque
    estoque.append(produto)

    print("Produto cadastrado com sucesso!\n")


# ----------------------------------------------------------
# Função para listar produtos
# ----------------------------------------------------------
def listar_produtos():
    print("\n=== Lista de Produtos ===")

    if not estoque:
        print("Nenhum produto cadastrado.\n")
        return

    for i, produto in enumerate(estoque):
        print(f"{i} - Nome: {produto['nome']}")
        print(f"    Preço: R$ {produto['preco']}")
        print(f"    Quantidade: {produto['quantidade']}")
        print("-" * 30)


# ----------------------------------------------------------
# Função para atualizar quantidade
# ----------------------------------------------------------
def atualizar_quantidade():
    listar_produtos()

    if not estoque:
        return

    indice = int(input("Digite o número do produto: "))
    nova_quantidade = int(input("Nova quantidade: "))

    estoque[indice]["quantidade"] = nova_quantidade

    print("Quantidade atualizada com sucesso!\n")


# ----------------------------------------------------------
# Função para remover produto
# ----------------------------------------------------------
def remover_produto():
    listar_produtos()

    if not estoque:
        return

    indice = int(input("Digite o número do produto para remover: "))

    produto_removido = estoque.pop(indice)

    print(f"Produto '{produto_removido['nome']}' removido com sucesso!\n")


# ----------------------------------------------------------
# Função principal (menu)
# ----------------------------------------------------------
def menu():

    while True:

        print("\n========== SISTEMA DE ESTOQUE ==========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar quantidade")
        print("4 - Remover produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            atualizar_quantidade()

        elif opcao == "4":
            remover_produto()

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ----------------------------------------------------------
# Execução do programa
# ----------------------------------------------------------
if __name__ == "__main__":
    menu()