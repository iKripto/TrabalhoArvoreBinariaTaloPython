import csv
import os

ARQUIVO = "clientes.csv"

# ------------------------------
# Classe da Árvore Binária
# ------------------------------
class No:
    def __init__(self, chave, pos):
        self.chave = chave
        self.pos = pos    # posição (linha) no CSV
        self.esq = None
        self.dir = None

def inserir(raiz, chave, pos):
    if raiz is None:
        return No(chave, pos)
    if chave < raiz.chave:
        raiz.esq = inserir(raiz.esq, chave, pos)
    elif chave > raiz.chave:
        raiz.dir = inserir(raiz.dir, chave, pos)
    return raiz

def buscar(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    if chave < raiz.chave:
        return buscar(raiz.esq, chave)
    return buscar(raiz.dir, chave)

# ------------------------------
# Funções para manipular CSV
# ------------------------------
def inicializar_csv():
    if not os.path.isfile(ARQUIVO):
        with open(ARQUIVO, 'w', newline='') as arq:
            writer = csv.writer(arq)
            writer.writerow(["codigo", "nome", "endereco", "cidade", "uf", "status"])

def inserir_cliente_csv():
    codigo = int(input("Codigo: "))
    nome = input("Nome: ")
    endereco = input("Endereco: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")

    # adiciona no CSV
    with open(ARQUIVO, 'a', newline='') as arq:
        writer = csv.writer(arq)
        writer.writerow([codigo, nome, endereco, cidade, uf, "1"])  # status=1 ativo

    # descobrir a linha em que foi salvo
    with open(ARQUIVO, 'r') as arq:
        linhas = list(csv.reader(arq))
        pos = len(linhas) - 1  # posição da linha (sem contar cabeçalho)

    return codigo, pos

def mostrar_cliente(pos):
    with open(ARQUIVO, 'r') as arq:
        leitor = list(csv.reader(arq))
        if pos < len(leitor):
            print("Dados do cliente:")
            print(f"Codigo: {leitor[pos][0]}")
            print(f"Nome: {leitor[pos][1]}")
            print(f"Endereco: {leitor[pos][2]}")
            print(f"Cidade: {leitor[pos][3]}")
            print(f"UF: {leitor[pos][4]}")
            print(f"Status: {leitor[pos][5]}")
        else:
            print("Posição inválida no CSV.")

# ------------------------------
# Programa Principal
# ------------------------------
def main():
    inicializar_csv()
    arvore = None

    while True:
        print("\n--- MENU ---")
        print("1. Inserir cliente")
        print("2. Buscar cliente")
        print("3. Sair")
        op = input("Escolha: ")

        if op == "1":
            codigo, pos = inserir_cliente_csv()
            arvore = inserir(arvore, codigo, pos)
            print(f"Cliente {codigo} inserido na linha {pos}.")
        elif op == "2":
            chave = int(input("Digite o codigo: "))
            no = buscar(arvore, chave)
            if no:
                mostrar_cliente(no.pos)
            else:
                print("Cliente não encontrado na árvore.")
        elif op == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
