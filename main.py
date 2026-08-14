# ==========================================
# SISTEMA DE CONTROLE DE ESTOQUE
# ==========================================

class Movimentacao:
    """Classe responsável por armazenar os dados de cada movimentação (entrada/saída)."""
    def __init__(self, quantidade, data, responsavel: str = None):
        self.quantidade = quantidade
        self.data = data
        self.responsavel = responsavel

    def __repr__(self):
        info = f'Quantidade: {self.quantidade}\nData: {self.data}\n'
        if self.responsavel:
            info += f'Responsavel: {self.responsavel}\n'
        return f"{info}"


class Produto:
    """Classe que representa o produto e gerencia suas movimentações de estoque."""
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        self.entradas = []
        self.saidas = []

    def __repr__(self):
        return f"Produto: {self.nome} | Estoque: {self.quantidade}\n"

    def exibir_historico(self):
        """Exibe o extrato detalhado de entradas e saídas do produto."""
        print(f"\n{'=' * 10} HISTÓRICO: {self.nome} {'=' * 10}")
        print(f"Estoque atual: {self.quantidade}\n")

        print(">>> ENTRADAS:")
        if not self.entradas:
            print("  Nenhuma entrada registrada.")
        else:
            for item in self.entradas:
                print(f"  - Data: {item.data} | Qtd: {item.quantidade}")

        print("\n>>> SAÍDAS:")
        if not self.saidas:
            print("  Nenhuma saída registrada.")
        else:
            for item in self.saidas:
                responsavel_str = f" | Resp: {item.responsavel}" if item.responsavel else ""
                print(f"  - Data: {item.data} | Qtd: {item.quantidade}{responsavel_str}")

        print("=" * 40 + "\n")

    def dar_entrada(self, quantidade, data):
        """Adiciona quantidade ao estoque e registra no histórico de entradas."""
        if quantidade <= 0:
            print(f'Quantidade {quantidade} é inválida, digite um valor positivo.\n')
            return
        registro = Movimentacao(quantidade, data)
        self.quantidade += quantidade
        self.entradas.append(registro)

    def dar_saida(self, quantidade, data, responsavel):
        """Remove quantidade do estoque e registra no histórico de saídas."""
        registro = Movimentacao((quantidade * -1), data, responsavel)
        self.quantidade -= quantidade
        self.saidas.append(registro)


# Lista de produtos pré-cadastrados
produtos = [
    Produto('Sabão em pó', 250),
    Produto('Detergente', 100),
    Produto('Desengordurante', 0),
    Produto('Esponja de Aço', 1050)
]


# ==========================================
# FUNÇÕES DE ENTRADA E VALIDAÇÃO DE DADOS
# ==========================================

def obter_opcao_valida(minimo, maximo):
    """Valida a opção numérica selecionada no menu."""
    while True:
        entrada = input(f"Digite a opção desejada ({minimo}-{maximo}): ")
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(f"Opção inválida! Digite um número entre {minimo} e {maximo}.\n")
        except (ValueError, TypeError):
            print("Valor inválido! Digite um número inteiro.\n")


def listar_produtos_cadastrados():
    """Imprime a lista de produtos com seus respectivos índices."""
    print("\n--- Produtos Disponíveis ---")
    for i, prod in enumerate(produtos):
        print(f"[{i}] {prod.nome} (Estoque: {prod.quantidade})")


def obter_produto_valido():
    """Garante a seleção de um índice de produto existente na lista."""
    while True:
        listar_produtos_cadastrados()
        entrada = input("Escolha o número do produto: ")
        try:
            valor = int(entrada)
            if 0 <= valor < len(produtos):
                return valor
            print(f"Produto inválido! Escolha um valor entre 0 e {len(produtos) - 1}.\n")
        except (ValueError, TypeError):
            print("Entrada inválida! Digite um número inteiro.\n")


def listar_produtos():
    """Menu para consulta de histórico detalhado de um produto."""
    listar_produtos_cadastrados()
    entrada = input("Escolha o número do produto para ver detalhes (ou 's' para voltar): ")
    if entrada.lower() == 's':
        return
    try:
        opcao = int(entrada)
        if 0 <= opcao < len(produtos):
            produtos[opcao].exibir_historico()
        else:
            print(f"Opção inválida! Escolha entre 0 e {len(produtos) - 1}.\n")
    except (ValueError, TypeError):
        print("Opção inválida!\n")


def obter_quantidade_valida():
    """Garante que a quantidade informada seja um número inteiro positivo."""
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.\n")
            else:
                return quantidade
        except (ValueError, TypeError):
            print("Quantidade inválida! Digite um número inteiro.\n")


def obter_data():
    """Coleta e valida dia, mês e ano, retornando formatado em DD/MM/AAAA."""
    while True:
        try:
            dia = int(input("Entre com o dia (1-31): "))
            if 1 <= dia <= 31:
                break
            print("Dia inválido! Digite entre 1 e 31.\n")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.\n")

    while True:
        try:
            mes = int(input("Entre com o mês (1-12): "))
            if 1 <= mes <= 12:
                break
            print("Mês inválido! Digite entre 1 e 12.\n")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.\n")

    while True:
        try:
            ano = int(input("Entre com o ano (a partir de 2000): "))
            if ano >= 2000:
                break
            print("Ano inválido! Digite um ano a partir de 2000.\n")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.\n")

    return f"{dia:02d}/{mes:02d}/{ano}"


# ==========================================
# FLUXO PRINCIPAL DO PROGRAMA
# ==========================================

print('-' * 50)
print('Bem-vindo ao Administrador de Estoque!')
print('-' * 50)

while True:
    print('\nMenu Principal:')
    print('1 - Consultar histórico de produto')
    print('2 - Adicionar ao estoque (Entrada)')
    print('3 - Remover do estoque (Saída)')
    print('4 - Sair')

    valor_opcao = obter_opcao_valida(1, 4)

    if valor_opcao == 1:
        listar_produtos()

    elif valor_opcao == 2:
        print("\n--- REGISTRO DE ENTRADA ---")
        idx_prod = obter_produto_valido()
        qtd = obter_quantidade_valida()
        data = obter_data()
        produtos[idx_prod].dar_entrada(qtd, data)
        print(f"\nEntrada realizada com sucesso! Novo saldo:")
        print(produtos[idx_prod])

    elif valor_opcao == 3:
        print("\n--- REGISTRO DE SAÍDA ---")
        idx_prod = obter_produto_valido()
        qtd = obter_quantidade_valida()

        # Validação de estoque suficiente
        if qtd > produtos[idx_prod].quantidade:
            print(f"\n[ERRO] Quantidade solicitada ({qtd}) é maior que o estoque atual ({produtos[idx_prod].quantidade})!")
            continue

        data = obter_data()
        colaborador = input("Digite o nome do responsável: ")
        produtos[idx_prod].dar_saida(qtd, data, colaborador)
        print(f"\nSaída registrada com sucesso! Novo saldo:")
        print(produtos[idx_prod])

    elif valor_opcao == 4:
        print('\nEncerrando o sistema...')
        break