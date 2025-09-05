"""
Trabalho 2 ADS - T1 - Data de entrega: 08/10/2025

Trabalho Prático – Estruturas de Arquivos Indexados
Tema: Sistema de Gestão para Biblioteca – Arquivos Indexados em Python

Descrição do Trabalho: Neste projeto, você deve desenvolver um sistema de gestão para uma Biblioteca utilizando a lógica de arquivos indexados. 
Você será responsável por simular um  banco de dados simples para uma Biblioteca precisa de um sistema para controlar os livros disponíveis, os empréstimos feitos pelos alunos e os prazos de devolução, evitando perda de informações e possibilitando geração de relatórios.
Para isso:
A área de índices deve ser implementada como uma  Árvore Binária, que será armazenada em memória.
A área de dados deve ser armazenada em disco (arquivo de texto ou binário), garantindo que as informações fiquem salvas entre as execuções.
O programa deverá ser escrito em Python, com boa usabilidade, interface amigável e menus bem estruturados.

Implementar as tabelas (estruturas de dados), cada uma gravada em arquivo separado:

Cidades: Código da Cidade, Descrição, Estado
Cursos: Código do Curso, Descrição
Alunos: Cod_Aluno, nome, cod_curso, cod_cidade
Autores: Cod_Autor, nome, cod_cidade
Categorias: Código Categoria, Descrição
Livros: Cod_Livro, título, Cod_Autor, cod_categoria, ano_publicação, disponibilidade
Empréstimos: Cod_Emprestimo, Cod_Livro, Cod_Aluno, data_empréstimo, data devolução, devolvido

Implementar as seguintes funcionalidades:

1) Operações básicas
1.1) Inclusão de novos registros nas tabelas.
1.2) Consulta de registros das tabelas.
1.3) Exclusão de registros das tabelas.
1.4) Leitura exaustiva das tabelas.
A busca, inclusão e exclusão devem ser realizadas utilizando o índice em árvore binária.

2) Ao exibir um aluno na tabela Alunos, o programa deverá buscar o código do curso na tabela de Cursos e exibir a Descrição.
2.1) Buscar o código da cidade na tabela de Cidades e exibir a Descrição e o Estado.

3) Ao exibir um autor na tabela Autores, o programa deverá buscar o código da cidade na tabela de Cidades e exibir o nome da cidade e o Estado.

4) Ao incluir ou consultar dados na Tabela Livros, o programa deverá:
4.1) Buscar o código do autor na tabela Autores e exibir o nome do autor e o nome e estado de sua cidade.
4.2) Buscar o código da categoria na tabela Categorias e exibir a descrição da categoria.
4.3) O atributo disponibilidade serve para indicar se o livro está disponível para empréstimo ou se já está emprestado.

5) Ao incluir ou consultar dados na Tabela Empréstimos, o programa deverá:
5.1) Solicitar o código do livro e verificar na tabela Livros se o mesmo encontra-se disponível para empréstimo. Se não estiver disponível, emitir uma mensagem e não solicitar os demais dados.
5.2) Exibir o nome do livro e o nome da categoria.
5.3) Buscar o código do aluno na tabela Alunos e exibir seu nome e o nome de sua cidade.
5.4) A data do empréstimo deverá ser a data do dia atual e a data de devolução deverá ser 7 dias além da data atual.
5.5) Após a confirmação do empréstimo, marcar a disponibilidade do livro como "emprestado" e o atributo devolvido como "Não".

6) Permitir a realização da devolução do livro:
6.1) Verificar na tabela de empréstimos se o livro encontra-se dentro do prazo de devolução. Se estiver atrasado, exibir uma mensagem.
6.2) Após a confirmação da devolução, marcar a disponibilidade do livro como "disponível" e marcar o atributo devolvido como "Sim".

7) Permitir as seguintes consultas:
7.1) Livros que estão emprestado 
7.2) Livros que estão com a devolução atrasada 
7.3) Quantidade de livros emprestados por período (data inicial e data final) 

8) Ler todos os registros da tabela de Livros e exibi-los em ordem crescente de Código do Livro. Os seguintes dados deverão ser mostrados:
Cod_Livro, título, Nome do Autor, Nome da Categoria, disponibilidade
Ao final, mostrar a quantidade livros disponíveis e a quantidade total de livros que estão emprestados.

Observação importante: O trabalho deverá ser desenvolvido integralmente pelos alunos, sendo vedado o uso de ferramentas de geração automática de código (como ChatGPT, Copilot ou similares). 
Para garantir a aprendizagem, a avaliação será feita por meio de apresentações individuais onde cada aluno deve explicar partes específicas do 
código desenvolvido, as decisões de projeto tomadas, o funcionamento da estrutura de arquivos indexados e da árvore binária,
trechos do código, as dificuldades encontradas e como foram resolvidas.
"""


class cidade:
    def __init__(self, codigo_cidade, descricao_cidade, estado):
        self.codigo_cidade = codigo_cidade
        self.descricao = descricao_cidade
        self.estado = estado

class curso:
    def __init__ (self, codigo_curso, descricao_curso):
        self.codigo_curso = codigo_curso
        self.descricao_curso = descricao_curso
        