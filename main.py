class Movimentacao:
    def __init__(self, quantidade, data, responsavel: str = None):
        self.quantidade = quantidade
        self.data = data
        self.responsavel = responsavel

    def __repr__(self):
        info = f'Quantidade: {self.quantidade}\n Data: {self.data}\n'
        if self.responsavel:
            info += f'Responsavel: {self.responsavel}\n'
        return f"{info}"

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        self.entradas = []
        self.saidas = []
    def __repr__(self):
        info = f'Produto: {self.nome}\nEstoque: {self.quantidade}\n'
        return f"{info}"

    def exibir_historico(self):
        print(f"\n{'=' * 10} HISTÓRICO: {self.nome} {'=' * 10}")
        print(f"Estoque atual: {self.quantidade}\n")

        print(">>> ENTRADAS:")
        if not self.entradas:
            print("  Nenhuma entrada registrada.")
        else:
            for item in self.entradas:
                # O f-string com o objeto chama o __repr__ da Movimentacao
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
        if(quantidade <= 0):
            return f'Quantidade {quantidade} é inválida, digite um valor positivo\n'
        registro = Movimentacao(quantidade, data)
        self.quantidade += quantidade
        self.entradas.append(registro)

    def dar_saida(self, quantidade, data, responsavel):
        registro = Movimentacao((quantidade * -1), data, responsavel)
        self.quantidade -= quantidade
        self.saidas.append(registro)

produtos = [Produto('Sabão em pó', 250), Produto('Detergente', 100), Produto('Desengordurante', 0), Produto('Esponja de Aço', 1050)]


def obter_opcao_valida(minimo, maximo):
    while True:
        entrada = input(f"Digite uma opção ou aperte {maximo} para sair: ")

        try:
            valor = int(entrada)

            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Valor inválido! Digite um número entre {minimo} e {maximo -1}  ou {maximo} para sair.\n")

        except (ValueError, TypeError):
            print("Valor inválido! O valor digitado não é um número inteiro.\n")

def obter_produto_valido():
    while True:
        listar_produtos_para_soma()
        entrada = input(f"Escolha um produto da lista: ")
        try:
            valor = int(entrada)
            if valor >= 0 and valor <= len(produtos) -1:
                return valor
            else:
                print(f"Produto inválido, digite um produto da lista entre {0} e {len(produtos) -1}")
        except (ValueError, TypeError):
            print("Quantidade inválida! A quantidade digitada não é um número inteiro.\n")



def listar_produtos():
    contador = 0;
    while contador < len(produtos):
        produtos[contador].exibir_historico()
        contador += 1

def listar_produtos_para_soma():
    contador = 0;
    while contador < len(produtos):
        print(f'Produto N-{contador}: {produtos[contador].nome}')
        contador += 1
    return contador

def obter_quantidade_valida():
    while True:
        try:
            quantidade = int(input(f"Digite uma quantidade do produto: "))
            if quantidade <= 0:
                print("Digite um valor válido")
            else:
                return quantidade
        except (ValueError, TypeError):
            print("Quantidade inválida! A quantidade digitada não é um número inteiro.\n")

def obter_data():
    # 1. Validação do Dia
    while True:
        entrada = input("Entre com o dia (1-31): ")
        try:
            dia = int(entrada)
            if 1 <= dia <= 31:
                break
            print("Dia inválido! Digite um número entre 1 e 31.\n")
        except (ValueError, TypeError):
            print("Valor inválido! Digite um número inteiro.\n")

    # 2. Validação do Mês
    while True:
        entrada = input("Entre com o mês (1-12): ")
        try:
            mes = int(entrada)
            if 1 <= mes <= 12:
                break
            print("Mês inválido! Digite um número entre 1 e 12.\n")
        except (ValueError, TypeError):
            print("Valor inválido! Digite um número inteiro.\n")

    # 3. Validação do Ano
    while True:
        entrada = input("Entre com o ano (4 dígitos, maior que 1999): ")
        try:
            ano = int(entrada)
            if ano >= 2000:
                break
            print("Ano inválido! Digite um ano a partir de 2000.\n")
        except (ValueError, TypeError):
            print("Valor inválido! Digite um número inteiro.\n")


    return f"{dia:02d}/{mes:02d}/{ano}"


print(50* '-')
print('Bem vindo ao administrador de estoque!\n')


valor_opcao = 0

while valor_opcao != 4:

    print('Escolha uma opção: ')
    print('1 - Listar produtos')
    print('2 - Adicionar ao estoque')
    print('3 - Remover estoque')
    print('4 - Sair')

    valor_opcao = obter_opcao_valida(1,4)
    if valor_opcao == 1:
        listar_produtos()
    if valor_opcao == 2:
        produto_valido = obter_produto_valido()
        quantidade = obter_quantidade_valida()
        data = obter_data()
        produtos[produto_valido].dar_entrada( quantidade, data)
        print(produtos[produto_valido])
    if valor_opcao == 3:
        produto_valido = obter_produto_valido()
        quantidade = obter_quantidade_valida()
        if quantidade > produtos[produto_valido].quantidade:
            print(f"A quantidade foi digitada é maior que a quantidade em estoque!\nQuantidade: {quantidade}\nEstoque: {produtos[produto_valido].quantidade}")
            continue
        data = obter_data()
        colaborador = input("Digite o nome do colaborador: ")
        produtos[produto_valido].dar_saida(quantidade, data, colaborador)
        print(produtos[produto_valido])

    if valor_opcao == 4:
        print('Encerrando...')
        break

