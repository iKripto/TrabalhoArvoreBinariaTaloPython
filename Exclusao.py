MAX = 99
VETOR = []
TOTAL = 0
ARVORE = None

class Cliente:
    def __init__(self, codigo, nome, endereco, cidade, uf, status='1'):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf
        self.status = status


class Indice:
    def __init__(self, codigo, endereco, status='1'):
        self.codigo = codigo
        self.endereco = endereco
        self.esquerda = None
        self.direita = None 
        self.status = status


def inserir(raiz, codigo, endereco):
    if raiz is None:
        return Indice(codigo, endereco)
    elif codigo < raiz.codigo:
        raiz.esquerda = inserir(raiz.esquerda, codigo, endereco)
    elif codigo > raiz.codigo:
        raiz.direita = inserir(raiz.direita, codigo, endereco)
        return raiz


def buscar(raiz, codigo):
    if raiz is None:
        return -1
    if codigo == raiz.codigo and raiz.status == '1':
        return raiz.endereco
    elif codigo < raiz.codigo:
        return buscar(raiz.esquerda, codigo)
    else:
        return buscar(raiz.direita, codigo)


def excluir(raiz, codigo):
    if codigo == raiz.codigo and raiz.status == '1':
        raiz.status = '0'
        print("Cliente excluido")
    elif codigo == raiz.codigo and raiz.status == '0':
        print("Cliente ja foi excluido")
        return raiz
    elif codigo < raiz.codigo:
        return excluir(raiz.esquerda, codigo)
    else:
        return excluir(raiz.direita, codigo)


while True:
    print("1 inserir cliente")
    print("2 buscar cliente")
    print("3 excluir cliente")
    print("0 sair")
    opcao = int(input("selecione uma opcao: "))

    if opcao == 1:
        if TOTAL >= MAX:
            print("overflow")
            continue

        codigo = int(input("codigo: "))
        nome = input("nome: ")
        endereco = input("endereco: ")
        cidade = input("cidade: ")
        uf = input("uf: ")

        VETOR.append(Cliente(codigo, nome, endereco, cidade, uf))
        ARVORE = inserir(ARVORE, codigo, TOTAL)
        print(f"cliente inserido na posicao {TOTAL}.")
        TOTAL += 1

    elif opcao == 2:
        cod = int(input("digite o codigo para busca: "))
        pos = buscar(ARVORE, cod)
        if pos == -1:
            print("nao encontrado")
        else:
            print("cliente encontrado")
            print("nome:", VETOR[pos].nome)
            print("endereco:", VETOR[pos].endereco)
            print("cidade:", VETOR[pos].cidade)
            print("uf:", VETOR[pos].uf)

    elif opcao == 3:
        cod = int(input("digite o codigo para exclusao: "))
        ARVORE = excluir(ARVORE, cod)

    elif opcao == 0:
        break

print("programa fechado")
