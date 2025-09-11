# Trabalho final da disciplina de Classificação e Pesquisa de Dados.
# Entrada: Arquivo de texto com dados sobre trabalhos acadêmicos.
# Saída: Arquivos binários com dados e um arquivo de texto com os dados pedidos.

import os
from CSVF import *

# Funções
# ==================================================================================================================================

def switch(menu, handler, exit):
    #implementação de menu com iteração caso usuário faça escolhas erradas.
    while menu != 0:
        if menu == 1:
            print("Listagem de artigos de um autor.\n")
            exit.write("Listagem de artigos de um autor.\n")
            
            author(handler, input("Nome: "), exit)
            break
        elif menu == 2:
            print("Listagem de artigos de um conjunto de autores.\n")
            exit.write("Listagem de artigos de um conjunto de autores.\n")
            
            autores(handler, exit)
            break
        elif menu == 3:
            print("Listagem de artigos com palavra consultada no título.\n")
            exit.write("Listagem de artigos com palavra consultada no título.\n")
            
            title(handler, input("Palavra: "), exit)
            break
        elif menu == 4:
            print("Listagem ordenado por autor, do número de artigos do autor nessa área.\n")
            exit.write("Listagem ordenado por autor, do número de artigos do autor nessa área.\n")
            
            area(handler, input("Area: "), exit)
            break
        elif menu == 5:
            print("Listagem por ano.\n")
            exit.write("Listagem por ano.\n")

            year(handler, input("Ano: "), exit)
            break
        else:
            print("Valor inválido, tente novamente.")
            return 0
    if menu == 0:
        print("TCHAU!\n")
        exit.write("Arquivo Fechado.\n")
        exit.close()
        
    return 0
    
     
def autores(handler, exit):
    #função em que o usuário digita a entrada de mais de um autor.
    listadeautores = [] 
    simounao = ""

    f = open(handler + "data_authors_index.bin", 'rb')

    tree = pickle.load(f)


    simounao = input("\n(Quando terminar digite apenas n)\nDigite o nome dos autores (nome completo): \n")

    simounao = simounao.lower()

    if simounao != 'n':
        listadeautores.append(simounao)

    while simounao != "n":

        simounao = input()
        simounao = simounao.lower()


        if simounao != "n":
           
            listadeautores.append(simounao)

    if len(listadeautores) > 0:
        list_art = search_authors(listadeautores, tree, handler)
        
        print_list(list_art)

        if list_art != None:
            for i in list_art:
                r = i.__repr__()
                exit.write(r + "\n")

def author(name_archive, word_author, exit):
    #função lê o arquivo e retorna os dados do autor
    #Função printa dados do autor.
    list_art = []

    f = open(name_archive + "data_authors_index.bin", 'rb')

    tree = pickle.load(f)

    word_author = word_author.lower()

    list_art = list_article(word_author, tree, name_archive)

    print_list(list_art)

    if list_art != None:
        for i in list_art:
            r = i.__repr__()
            exit.write(r + "\n")

    f.close()


def title(name_archive, word, exit):
    #Busca palavra consultada.
    #Imprime todos os artigos com a palavra consultada.
    list_art = []

    f = open(name_archive + "data_word_index.bin", 'rb')

    tree = pickle.load(f)

    word = word.lower()

    list_art = list_article(word, tree, name_archive)

    print_list(list_art)

    if list_art != None:
        for i in list_art:
            r = i.__repr__()
            exit.write(r + "\n")

    f.close()

def area(name_archive, word_area, exit):
    #imprime, ordenado por autor, o número de artigos do autor nessa área.

    f = open(name_archive + "data_area_index.bin", 'rb')

    tree = pickle.load(f)

    word_area = word_area.lower()

    dictio = search_area(word_area, tree, name_archive)

    if dictio != None:
        l = list(dictio)

        l.sort()

        for author in l:
            print("\n" + author + ":\t\t\t" + str(dictio[author]))
            print("\n\n")
    else:
        print("\nResultado não encontrado.\n")


def year(name_archive, year, exit):
    #lista artigos por idioma
    list_art = []

    f = open(name_archive + "data_year_index.bin", 'rb')

    tree = pickle.load(f)

    list_art = list_article(year, tree, name_archive)

    print_list(list_art)

    if list_art != None:
        for i in list_art:
            r = i.__repr__()
            exit.write(r + "\n")

    f.close()

def verify_entry (nomedaentrada):
    try:
        entrada = open(nomedaentrada+"data_authors_index.bin", "wb")
        print("\nArquivo já processado anteriormente\n")
        entrada.close()
        return True
    except:
        print("\nArquivo novo.\nVamos processar o arquivo pela primeira vez.\nAguarde\n")
        return False

def test():
    try:
        handler = input("File name:")
        f = open(handler + ".csv", 'r', errors='ignore', encoding = "UTF-8")
        return [f, handler]

    except:
        print("\nEste arquivo não existe, tente de novo\n")
        return test()
   
#MAIN 
#---------------------------------------------------------------------------------
Registers = []
files = []

k = test()

f = k[0]

handler = k[1]

del k
# parte de processamento do arquivo.
offset = 0

if os.path.isfile(handler + 'Data.bin') == False:
    with open(handler + 'Data.bin', "wb") as handler_data:
        for line in csv.reader(f, dialect='excel', delimiter=';'):
            if line[0] == "ano":                #se for a primeira linha, ignora
                del line
            else:
                i = 21
                for element in line[21::1]:
                    i += 1
                    if element == "":
                        del line[i-1::]
                newElement = Register(offset, line)
                Registers.append(newElement)
                pickle.dump(newElement, handler_data, pickle.HIGHEST_PROTOCOL)

                #offset += newElement.nbytes  #Em teste
                offset += 1

    f.close()

    make_index_files(Registers, handler)

print("\nArquivo " + handler + " aberto e processado com sucesso\n")

arquivodesaida = input("\nPara melhor visualizar os dados, tudo será impresso em um arquivo de saida. \nPor favor, escolha um nome para este arquivo.\n")
arquivodesaida = arquivodesaida + ".txt"
print(arquivodesaida + " criado\n")
saida = open(arquivodesaida, "w")


menu = 1
while menu != 0:
    print("Escolha uma das opções abaixo:\n\n")
    print("[1] Listagem de artigos de um autor.\n")
    print("[2] Listagem de artigos de um conjunto de autores.\n")
    print("[3] Listagem de artigos com palavra consultada no título.\n")
    print("[4] Listagem do número de artigos, por autor, de uma área.\n")
    print("[5] Listagem por ano.\n")
    print("[0] Finalizar programa.\n")
    menu = int(input()) #input recebe um string, precisamos transformar em inteiro.
    switch(menu, handler, saida)
    input()