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

    def dar_entrada(self, quantidade, data):
        registro = Movimentacao(quantidade, data)
        self.quantidade += quantidade
        self.entradas.append(registro)

    def dar_saida(self, quantidade, data, responsavel):
        registro = Movimentacao((quantidade * -1), data, responsavel)
        self.quantidade -= quantidade
        self.saidas.append(registro)

produtos = [Produto('Sabão em pó', 250), Produto('Detergente', 100), Produto('Desengordurante', 0), Produto('Esponja de Aço', 1050)]


def obter_valor_valido(minimo, maximo):
    while True:
        entrada = input(f"Digite uma opção ou aperte {maximo} para sair: ")

        try:
            valor = int(entrada)

            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Valor inválido! Digite um número entre {minimo} e {maximo}.\n")

        except (ValueError, TypeError):
            print("Valor inválido! O valor digitado não é um número inteiro.\n")


def listar_produtos():
    contador = 0;
    while contador < len(produtos):
        print(f'Produto N-{contador} : {produtos[contador].nome}\n[Estoque: {produtos[contador].quantidade}]')
        contador += 1

def listar_produtos_resumido():
    contador = 0;
    while contador < len(produtos):
        print(f'Produto N-{contador}: {produtos[contador].nome}')
        contador += 1

print(50* '-')
print('Bem vindo ao administrador de estoque!\n')
print('Escolha uma opção: ')
print('1 - Listar produtos')
print('2 - Adicionar ao estoque')
print('3 - Remover estoque')
print('4 - Sair')

valor_opcao = 0

while valor_opcao != 4:

    valor_opcao = obter_valor_valido(1,4)
    if valor_opcao == 1:
        listar_produtos()
    if valor_opcao == 2:
        listar_produtos_resumido()
    if valor_opcao == 4:
        print('Encerrando...')
        break

