import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, timedelta
import csv
import os

class BibliotecaFrontend:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão para Biblioteca")
        self.root.geometry("1000x700")
        
        # Carregar dados das tabelas
        self.tabelas = {
            'cidades': self.carregar_tabela('cidades.csv'),
            'cursos': self.carregar_tabela('cursos.csv'),
            'alunos': self.carregar_tabela('alunos.csv'),
            'autores': self.carregar_tabela('autores.csv'),
            'categorias': self.carregar_tabela('categorias.csv'),
            'livros': self.carregar_tabela('livros.csv'),
            'emprestimos': self.carregar_tabela('emprestimos.csv')
        }
        
        # Configurar interface
        self.setup_interface()
        
    def carregar_tabela(self, nome_arquivo):
        if not os.path.exists(nome_arquivo):
            return []
        
        dados = []
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha.get('ativo', '1') == '1':
                    dados.append(linha)
        return dados
    
    def salvar_tabela(self, nome_arquivo, dados, colunas):
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)
            escritor.writeheader()
            for linha in dados:
                escritor.writerow(linha)
    
    def setup_interface(self):
        # Criar abas para diferentes funcionalidades
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Abas
        self.frame_principal = ttk.Frame(self.notebook)
        self.frame_cidades = ttk.Frame(self.notebook)
        self.frame_cursos = ttk.Frame(self.notebook)
        self.frame_alunos = ttk.Frame(self.notebook)
        self.frame_autores = ttk.Frame(self.notebook)
        self.frame_categorias = ttk.Frame(self.notebook)
        self.frame_livros = ttk.Frame(self.notebook)
        self.frame_emprestimos = ttk.Frame(self.notebook)
        self.frame_devolucoes = ttk.Frame(self.notebook)
        self.frame_consultas = ttk.Frame(self.notebook)
        
        self.notebook.add(self.frame_principal, text="Principal")
        self.notebook.add(self.frame_cidades, text="Cidades")
        self.notebook.add(self.frame_cursos, text="Cursos")
        self.notebook.add(self.frame_alunos, text="Alunos")
        self.notebook.add(self.frame_autores, text="Autores")
        self.notebook.add(self.frame_categorias, text="Categorias")
        self.notebook.add(self.frame_livros, text="Livros")
        self.notebook.add(self.frame_emprestimos, text="Empréstimos")
        self.notebook.add(self.frame_devolucoes, text="Devoluções")
        self.notebook.add(self.frame_consultas, text="Consultas")
        
        # Configurar cada aba
        self.configurar_aba_principal()
        self.configurar_aba_cidades()
        self.configurar_aba_cursos()
        self.configurar_aba_alunos()
        self.configurar_aba_autores()
        self.configurar_aba_categorias()
        self.configurar_aba_livros()
        self.configurar_aba_emprestimos()
        self.configurar_aba_devolucoes()
        self.configurar_aba_consultas()
    
    def configurar_aba_principal(self):
        lbl_titulo = ttk.Label(self.frame_principal, text="Sistema de Gestão para Biblioteca", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=20)
        
        lbl_descricao = ttk.Label(self.frame_principal, text="Selecione uma aba acima para gerenciar os diferentes aspectos do sistema", font=("Arial", 12))
        lbl_descricao.pack(pady=10)
        
        # Estatísticas rápidas
        frame_stats = ttk.LabelFrame(self.frame_principal, text="Estatísticas")
        frame_stats.pack(fill="x", padx=20, pady=10)
        
        livros_total = len(self.tabelas['livros'])
        livros_disponiveis = len([l for l in self.tabelas['livros'] if l['disponibilidade'] == 'disponível'])
        livros_emprestados = livros_total - livros_disponiveis
        
        ttk.Label(frame_stats, text=f"Total de Livros: {livros_total}").pack(anchor="w", padx=10, pady=5)
        ttk.Label(frame_stats, text=f"Livros Disponíveis: {livros_disponiveis}").pack(anchor="w", padx=10, pady=5)
        ttk.Label(frame_stats, text=f"Livros Emprestados: {livros_emprestados}").pack(anchor="w", padx=10, pady=5)
        ttk.Label(frame_stats, text=f"Total de Alunos: {len(self.tabelas['alunos'])}").pack(anchor="w", padx=10, pady=5)
        ttk.Label(frame_stats, text=f"Total de Empréstimos Ativos: {len([e for e in self.tabelas['emprestimos'] if e['devolvido'] == 'Não'])}").pack(anchor="w", padx=10, pady=5)
    
    def configurar_aba_cidades(self):
        # Frame para formulário
        frame_form = ttk.LabelFrame(self.frame_cidades, text="Adicionar/Editar Cidade")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Descrição:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_descricao = ttk.Entry(frame_form)
        entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Estado:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_estado = ttk.Entry(frame_form)
        entry_estado.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_cidade(
            entry_codigo.get(), entry_descricao.get(), entry_estado.get()))
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Frame para lista
        frame_lista = ttk.LabelFrame(self.frame_cidades, text="Lista de Cidades")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Descrição", "Estado")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Descrição", width=200)
        
        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        # Popular a treeview
        for cidade in self.tabelas['cidades']:
            tree.insert("", "end", values=(cidade['codigo'], cidade['descricao'], cidade['estado']))
        
        # Botão para excluir
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'cidades', 'codigo'))
        btn_excluir.pack(pady=5)
    
    def salvar_cidade(self, codigo, descricao, estado):
        if not codigo or not descricao or not estado:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Verificar se já existe
        for i, cidade in enumerate(self.tabelas['cidades']):
            if cidade['codigo'] == codigo:
                # Atualizar
                self.tabelas['cidades'][i] = {
                    'codigo': codigo,
                    'descricao': descricao,
                    'estado': estado,
                    'ativo': '1'
                }
                self.salvar_tabela('cidades.csv', self.tabelas['cidades'], ['codigo', 'descricao', 'estado', 'ativo'])
                messagebox.showinfo("Sucesso", "Cidade atualizada com sucesso!")
                self.recarregar_aba('cidades')
                return
        
        # Adicionar nova cidade
        self.tabelas['cidades'].append({
            'codigo': codigo,
            'descricao': descricao,
            'estado': estado,
            'ativo': '1'
        })
        self.salvar_tabela('cidades.csv', self.tabelas['cidades'], ['codigo', 'descricao', 'estado', 'ativo'])
        messagebox.showinfo("Sucesso", "Cidade adicionada com sucesso!")
        self.recarregar_aba('cidades')
    
    def configurar_aba_cursos(self):
        # Implementação similar à aba cidades
        frame_form = ttk.LabelFrame(self.frame_cursos, text="Adicionar/Editar Curso")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Descrição:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_descricao = ttk.Entry(frame_form)
        entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_curso(
            entry_codigo.get(), entry_descricao.get()))
        btn_salvar.grid(row=2, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_cursos, text="Lista de Cursos")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Descrição")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Descrição", width=300)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for curso in self.tabelas['cursos']:
            tree.insert("", "end", values=(curso['codigo'], curso['descricao']))
        
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'cursos', 'codigo'))
        btn_excluir.pack(pady=5)
    
    def salvar_curso(self, codigo, descricao):
        if not codigo or not descricao:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        for i, curso in enumerate(self.tabelas['cursos']):
            if curso['codigo'] == codigo:
                self.tabelas['cursos'][i] = {
                    'codigo': codigo,
                    'descricao': descricao,
                    'ativo': '1'
                }
                self.salvar_tabela('cursos.csv', self.tabelas['cursos'], ['codigo', 'descricao', 'ativo'])
                messagebox.showinfo("Sucesso", "Curso atualizado com sucesso!")
                self.recarregar_aba('cursos')
                return
        
        self.tabelas['cursos'].append({
            'codigo': codigo,
            'descricao': descricao,
            'ativo': '1'
        })
        self.salvar_tabela('cursos.csv', self.tabelas['cursos'], ['codigo', 'descricao', 'ativo'])
        messagebox.showinfo("Sucesso", "Curso adicionado com sucesso!")
        self.recarregar_aba('cursos')
    
    def configurar_aba_alunos(self):
        # Implementação similar, mas com campos adicionais
        frame_form = ttk.LabelFrame(self.frame_alunos, text="Adicionar/Editar Aluno")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_nome = ttk.Entry(frame_form)
        entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Curso:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_cod_curso = ttk.Entry(frame_form)
        entry_cod_curso.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Cidade:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_cod_cidade = ttk.Entry(frame_form)
        entry_cod_cidade.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_aluno(
            entry_codigo.get(), entry_nome.get(), entry_cod_curso.get(), entry_cod_cidade.get()))
        btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_alunos, text="Lista de Alunos")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Nome", "Curso", "Cidade")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Nome", width=200)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for aluno in self.tabelas['alunos']:
            # Buscar informações do curso e cidade
            curso_desc = next((c['descricao'] for c in self.tabelas['cursos'] if c['codigo'] == aluno['cod_curso']), "Não encontrado")
            cidade_desc = next((c['descricao'] for c in self.tabelas['cidades'] if c['codigo'] == aluno['cod_cidade']), "Não encontrado")
            
            tree.insert("", "end", values=(aluno['cod_aluno'], aluno['nome'], curso_desc, cidade_desc))
        
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'alunos', 'cod_aluno'))
        btn_excluir.pack(pady=5)
    
    def salvar_aluno(self, codigo, nome, cod_curso, cod_cidade):
        if not codigo or not nome or not cod_curso or not cod_cidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        for i, aluno in enumerate(self.tabelas['alunos']):
            if aluno['cod_aluno'] == codigo:
                self.tabelas['alunos'][i] = {
                    'cod_aluno': codigo,
                    'nome': nome,
                    'cod_curso': cod_curso,
                    'cod_cidade': cod_cidade,
                    'ativo': '1'
                }
                self.salvar_tabela('alunos.csv', self.tabelas['alunos'], ['cod_aluno', 'nome', 'cod_curso', 'cod_cidade', 'ativo'])
                messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
                self.recarregar_aba('alunos')
                return
        
        self.tabelas['alunos'].append({
            'cod_aluno': codigo,
            'nome': nome,
            'cod_curso': cod_curso,
            'cod_cidade': cod_cidade,
            'ativo': '1'
        })
        self.salvar_tabela('alunos.csv', self.tabelas['alunos'], ['cod_aluno', 'nome', 'cod_curso', 'cod_cidade', 'ativo'])
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
        self.recarregar_aba('alunos')
    
    def configurar_aba_autores(self):
        # Implementação similar à aba alunos
        frame_form = ttk.LabelFrame(self.frame_autores, text="Adicionar/Editar Autor")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_nome = ttk.Entry(frame_form)
        entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Cidade:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_cod_cidade = ttk.Entry(frame_form)
        entry_cod_cidade.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_autor(
            entry_codigo.get(), entry_nome.get(), entry_cod_cidade.get()))
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_autores, text="Lista de Autores")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Nome", "Cidade")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Nome", width=200)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for autor in self.tabelas['autores']:
            cidade_desc = next((c['descricao'] for c in self.tabelas['cidades'] if c['codigo'] == autor['cod_cidade']), "Não encontrado")
            tree.insert("", "end", values=(autor['cod_autor'], autor['nome'], cidade_desc))
        
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'autores', 'cod_autor'))
        btn_excluir.pack(pady=5)
    
    def salvar_autor(self, codigo, nome, cod_cidade):
        if not codigo or not nome or not cod_cidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        for i, autor in enumerate(self.tabelas['autores']):
            if autor['cod_autor'] == codigo:
                self.tabelas['autores'][i] = {
                    'cod_autor': codigo,
                    'nome': nome,
                    'cod_cidade': cod_cidade,
                    'ativo': '1'
                }
                self.salvar_tabela('autores.csv', self.tabelas['autores'], ['cod_autor', 'nome', 'cod_cidade', 'ativo'])
                messagebox.showinfo("Sucesso", "Autor atualizado com sucesso!")
                self.recarregar_aba('autores')
                return
        
        self.tabelas['autores'].append({
            'cod_autor': codigo,
            'nome': nome,
            'cod_cidade': cod_cidade,
            'ativo': '1'
        })
        self.salvar_tabela('autores.csv', self.tabelas['autores'], ['cod_autor', 'nome', 'cod_cidade', 'ativo'])
        messagebox.showinfo("Sucesso", "Autor adicionado com sucesso!")
        self.recarregar_aba('autores')
    
    def configurar_aba_categorias(self):
        # Implementação similar à aba cidades
        frame_form = ttk.LabelFrame(self.frame_categorias, text="Adicionar/Editar Categoria")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Descrição:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_descricao = ttk.Entry(frame_form)
        entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_categoria(
            entry_codigo.get(), entry_descricao.get()))
        btn_salvar.grid(row=2, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_categorias, text="Lista de Categorias")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Descrição")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Descrição", width=300)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for categoria in self.tabelas['categorias']:
            tree.insert("", "end", values=(categoria['cod_categoria'], categoria['descricao']))
        
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'categorias', 'cod_categoria'))
        btn_excluir.pack(pady=5)
    
    def salvar_categoria(self, codigo, descricao):
        if not codigo or not descricao:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        for i, categoria in enumerate(self.tabelas['categorias']):
            if categoria['cod_categoria'] == codigo:
                self.tabelas['categorias'][i] = {
                    'cod_categoria': codigo,
                    'descricao': descricao,
                    'ativo': '1'
                }
                self.salvar_tabela('categorias.csv', self.tabelas['categorias'], ['cod_categoria', 'descricao', 'ativo'])
                messagebox.showinfo("Sucesso", "Categoria atualizada com sucesso!")
                self.recarregar_aba('categorias')
                return
        
        self.tabelas['categorias'].append({
            'cod_categoria': codigo,
            'descricao': descricao,
            'ativo': '1'
        })
        self.salvar_tabela('categorias.csv', self.tabelas['categorias'], ['cod_categoria', 'descricao', 'ativo'])
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")
        self.recarregar_aba('categorias')
    
    def configurar_aba_livros(self):
        # Implementação mais complexa com mais campos
        frame_form = ttk.LabelFrame(self.frame_livros, text="Adicionar/Editar Livro")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_codigo = ttk.Entry(frame_form)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Título:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_titulo = ttk.Entry(frame_form)
        entry_titulo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Autor:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_cod_autor = ttk.Entry(frame_form)
        entry_cod_autor.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Categoria:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_cod_categoria = ttk.Entry(frame_form)
        entry_cod_categoria.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Ano Publicação:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        entry_ano = ttk.Entry(frame_form)
        entry_ano.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Disponibilidade:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        combo_disponibilidade = ttk.Combobox(frame_form, values=["disponível", "emprestado"])
        combo_disponibilidade.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        combo_disponibilidade.set("disponível")
        
        btn_salvar = ttk.Button(frame_form, text="Salvar", command=lambda: self.salvar_livro(
            entry_codigo.get(), entry_titulo.get(), entry_cod_autor.get(), 
            entry_cod_categoria.get(), entry_ano.get(), combo_disponibilidade.get()))
        btn_salvar.grid(row=6, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_livros, text="Lista de Livros")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Título", "Autor", "Categoria", "Ano", "Disponibilidade")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=80)
        
        tree.column("Título", width=200)
        tree.column("Autor", width=150)
        tree.column("Categoria", width=150)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for livro in self.tabelas['livros']:
            autor_nome = next((a['nome'] for a in self.tabelas['autores'] if a['cod_autor'] == livro['cod_autor']), "Não encontrado")
            categoria_desc = next((c['descricao'] for c in self.tabelas['categorias'] if c['cod_categoria'] == livro['cod_categoria']), "Não encontrado")
            
            tree.insert("", "end", values=(
                livro['cod_livro'], 
                livro['titulo'], 
                autor_nome, 
                categoria_desc, 
                livro['ano_publicacao'], 
                livro['disponibilidade']
            ))
        
        btn_excluir = ttk.Button(frame_lista, text="Excluir Selecionado", 
                                command=lambda: self.excluir_registro(tree, 'livros', 'cod_livro'))
        btn_excluir.pack(pady=5)
    
    def salvar_livro(self, codigo, titulo, cod_autor, cod_categoria, ano, disponibilidade):
        if not codigo or not titulo or not cod_autor or not cod_categoria or not ano:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        for i, livro in enumerate(self.tabelas['livros']):
            if livro['cod_livro'] == codigo:
                self.tabelas['livros'][i] = {
                    'cod_livro': codigo,
                    'titulo': titulo,
                    'cod_autor': cod_autor,
                    'cod_categoria': cod_categoria,
                    'ano_publicacao': ano,
                    'disponibilidade': disponibilidade,
                    'ativo': '1'
                }
                self.salvar_tabela('livros.csv', self.tabelas['livros'], ['cod_livro', 'titulo', 'cod_autor', 'cod_categoria', 'ano_publicacao', 'disponibilidade', 'ativo'])
                messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
                self.recarregar_aba('livros')
                return
        
        self.tabelas['livros'].append({
            'cod_livro': codigo,
            'titulo': titulo,
            'cod_autor': cod_autor,
            'cod_categoria': cod_categoria,
            'ano_publicacao': ano,
            'disponibilidade': disponibilidade,
            'ativo': '1'
        })
        self.salvar_tabela('livros.csv', self.tabelas['livros'], ['cod_livro', 'titulo', 'cod_autor', 'cod_categoria', 'ano_publicacao', 'disponibilidade', 'ativo'])
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
        self.recarregar_aba('livros')
    
    def configurar_aba_emprestimos(self):
        frame_form = ttk.LabelFrame(self.frame_emprestimos, text="Realizar Empréstimo")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código Livro:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_cod_livro = ttk.Entry(frame_form)
        entry_cod_livro.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_form, text="Código Aluno:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_cod_aluno = ttk.Entry(frame_form)
        entry_cod_aluno.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        btn_emprestar = ttk.Button(frame_form, text="Realizar Empréstimo", command=lambda: self.realizar_emprestimo(
            entry_cod_livro.get(), entry_cod_aluno.get()))
        btn_emprestar.grid(row=2, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_emprestimos, text="Empréstimos Ativos")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Livro", "Aluno", "Data Empréstimo", "Data Devolução", "Devolvido")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Livro", width=150)
        tree.column("Aluno", width=150)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for emprestimo in self.tabelas['emprestimos']:
            if emprestimo['devolvido'] == 'Não':
                livro_titulo = next((l['titulo'] for l in self.tabelas['livros'] if l['cod_livro'] == emprestimo['cod_livro']), "Não encontrado")
                aluno_nome = next((a['nome'] for a in self.tabelas['alunos'] if a['cod_aluno'] == emprestimo['cod_aluno']), "Não encontrado")
                
                tree.insert("", "end", values=(
                    emprestimo['cod_emprestimo'],
                    livro_titulo,
                    aluno_nome,
                    emprestimo['data_emprestimo'],
                    emprestimo['data_devolucao'],
                    emprestimo['devolvido']
                ))
    
    def realizar_emprestimo(self, cod_livro, cod_aluno):
        if not cod_livro or not cod_aluno:
            messagebox.showerror("Erro", "Código do livro e do aluno são obrigatórios!")
            return
        
        # Verificar se o livro existe e está disponível
        livro = next((l for l in self.tabelas['livros'] if l['cod_livro'] == cod_livro), None)
        if not livro:
            messagebox.showerror("Erro", "Livro não encontrado!")
            return
        
        if livro['disponibilidade'] != 'disponível':
            messagebox.showerror("Erro", "Livro não disponível para empréstimo!")
            return
        
        # Verificar se o aluno existe
        aluno = next((a for a in self.tabelas['alunos'] if a['cod_aluno'] == cod_aluno), None)
        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado!")
            return
        
        # Gerar código de empréstimo
        cod_emprestimo = str(len(self.tabelas['emprestimos']) + 1)
        
        # Datas
        data_emprestimo = datetime.now().strftime('%Y-%m-%d')
        data_devolucao = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        
        # Adicionar empréstimo
        self.tabelas['emprestimos'].append({
            'cod_emprestimo': cod_emprestimo,
            'cod_livro': cod_livro,
            'cod_aluno': cod_aluno,
            'data_emprestimo': data_emprestimo,
            'data_devolucao': data_devolucao,
            'devolvido': 'Não',
            'ativo': '1'
        })
        
        # Atualizar disponibilidade do livro
        for i, l in enumerate(self.tabelas['livros']):
            if l['cod_livro'] == cod_livro:
                self.tabelas['livros'][i]['disponibilidade'] = 'emprestado'
                break
        
        # Salvar alterações
        self.salvar_tabela('emprestimos.csv', self.tabelas['emprestimos'], 
                          ['cod_emprestimo', 'cod_livro', 'cod_aluno', 'data_emprestimo', 'data_devolucao', 'devolvido', 'ativo'])
        self.salvar_tabela('livros.csv', self.tabelas['livros'], 
                          ['cod_livro', 'titulo', 'cod_autor', 'cod_categoria', 'ano_publicacao', 'disponibilidade', 'ativo'])
        
        messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
        self.recarregar_aba('emprestimos')
        self.recarregar_aba('livros')
    
    def configurar_aba_devolucoes(self):
        frame_form = ttk.LabelFrame(self.frame_devolucoes, text="Realizar Devolução")
        frame_form.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_form, text="Código Livro:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_cod_livro = ttk.Entry(frame_form)
        entry_cod_livro.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        btn_devolver = ttk.Button(frame_form, text="Realizar Devolução", command=lambda: self.realizar_devolucao(
            entry_cod_livro.get()))
        btn_devolver.grid(row=1, column=0, columnspan=2, pady=10)
        
        frame_lista = ttk.LabelFrame(self.frame_devolucoes, text="Histórico de Devoluções")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)
        
        colunas = ("Código", "Livro", "Aluno", "Data Empréstimo", "Data Devolução", "Devolvido")
        tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        tree.column("Livro", width=150)
        tree.column("Aluno", width=150)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        for emprestimo in self.tabelas['emprestimos']:
            if emprestimo['devolvido'] == 'Sim':
                livro_titulo = next((l['titulo'] for l in self.tabelas['livros'] if l['cod_livro'] == emprestimo['cod_livro']), "Não encontrado")
                aluno_nome = next((a['nome'] for a in self.tabelas['alunos'] if a['cod_aluno'] == emprestimo['cod_aluno']), "Não encontrado")
                
                tree.insert("", "end", values=(
                    emprestimo['cod_emprestimo'],
                    livro_titulo,
                    aluno_nome,
                    emprestimo['data_emprestimo'],
                    emprestimo['data_devolucao'],
                    emprestimo['devolvido']
                ))
    
    def realizar_devolucao(self, cod_livro):
        if not cod_livro:
            messagebox.showerror("Erro", "Código do livro é obrigatório!")
            return
        
        # Encontrar empréstimo ativo para este livro
        emprestimo = next((e for e in self.tabelas['emprestimos'] 
                          if e['cod_livro'] == cod_livro and e['devolvido'] == 'Não'), None)
        
        if not emprestimo:
            messagebox.showerror("Erro", "Não há empréstimo ativo para este livro!")
            return
        
        # Verificar se está atrasado
        data_devolucao = datetime.strptime(emprestimo['data_devolucao'], '%Y-%m-%d')
        if datetime.now() > data_devolucao:
            dias_atraso = (datetime.now() - data_devolucao).days
            messagebox.showwarning("Atraso", f"Devolução em atraso! Dias de atraso: {dias_atraso}")
        
        # Atualizar empréstimo
        for i, e in enumerate(self.tabelas['emprestimos']):
            if e['cod_emprestimo'] == emprestimo['cod_emprestimo']:
                self.tabelas['emprestimos'][i]['devolvido'] = 'Sim'
                break
        
        # Atualizar disponibilidade do livro
        for i, l in enumerate(self.tabelas['livros']):
            if l['cod_livro'] == cod_livro:
                self.tabelas['livros'][i]['disponibilidade'] = 'disponível'
                break
        
        # Salvar alterações
        self.salvar_tabela('emprestimos.csv', self.tabelas['emprestimos'], 
                          ['cod_emprestimo', 'cod_livro', 'cod_aluno', 'data_emprestimo', 'data_devolucao', 'devolvido', 'ativo'])
        self.salvar_tabela('livros.csv', self.tabelas['livros'], 
                          ['cod_livro', 'titulo', 'cod_autor', 'cod_categoria', 'ano_publicacao', 'disponibilidade', 'ativo'])
        
        messagebox.showinfo("Sucesso", "Devolução realizada com sucesso!")
        self.recarregar_aba('devolucoes')
        self.recarregar_aba('livros')
        self.recarregar_aba('emprestimos')
    
    def configurar_aba_consultas(self):
        notebook_consultas = ttk.Notebook(self.frame_consultas)
        notebook_consultas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Consulta 1: Livros emprestados
        frame_consulta1 = ttk.Frame(notebook_consultas)
        notebook_consultas.add(frame_consulta1, text="Livros Emprestados")
        
        colunas1 = ("Código", "Título", "Autor", "Categoria", "Ano")
        tree1 = ttk.Treeview(frame_consulta1, columns=colunas1, show="headings")
        
        for col in colunas1:
            tree1.heading(col, text=col)
            tree1.column(col, width=100)
        
        tree1.column("Título", width=200)
        tree1.column("Autor", width=150)
        
        scrollbar1 = ttk.Scrollbar(frame_consulta1, orient="vertical", command=tree1.yview)
        tree1.configure(yscrollcommand=scrollbar1.set)
        scrollbar1.pack(side="right", fill="y")
        tree1.pack(side="left", fill="both", expand=True)
        
        for livro in self.tabelas['livros']:
            if livro['disponibilidade'] == 'emprestado':
                autor_nome = next((a['nome'] for a in self.tabelas['autores'] if a['cod_autor'] == livro['cod_autor']), "Não encontrado")
                categoria_desc = next((c['descricao'] for c in self.tabelas['categorias'] if c['cod_categoria'] == livro['cod_categoria']), "Não encontrado")
                
                tree1.insert("", "end", values=(
                    livro['cod_livro'], 
                    livro['titulo'], 
                    autor_nome, 
                    categoria_desc, 
                    livro['ano_publicacao']
                ))
        
        # Consulta 2: Livros com devolução atrasada
        frame_consulta2 = ttk.Frame(notebook_consultas)
        notebook_consultas.add(frame_consulta2, text="Livros Atrasados")
        
        colunas2 = ("Código", "Livro", "Aluno", "Data Devolução", "Dias Atraso")
        tree2 = ttk.Treeview(frame_consulta2, columns=colunas2, show="headings")
        
        for col in colunas2:
            tree2.heading(col, text=col)
            tree2.column(col, width=100)
        
        tree2.column("Livro", width=150)
        tree2.column("Aluno", width=150)
        
        scrollbar2 = ttk.Scrollbar(frame_consulta2, orient="vertical", command=tree2.yview)
        tree2.configure(yscrollcommand=scrollbar2.set)
        scrollbar2.pack(side="right", fill="y")
        tree2.pack(side="left", fill="both", expand=True)
        
        hoje = datetime.now()
        for emprestimo in self.tabelas['emprestimos']:
            if emprestimo['devolvido'] == 'Não':
                data_devolucao = datetime.strptime(emprestimo['data_devolucao'], '%Y-%m-%d')
                if hoje > data_devolucao:
                    livro_titulo = next((l['titulo'] for l in self.tabelas['livros'] if l['cod_livro'] == emprestimo['cod_livro']), "Não encontrado")
                    aluno_nome = next((a['nome'] for a in self.tabelas['alunos'] if a['cod_aluno'] == emprestimo['cod_aluno']), "Não encontrado")
                    dias_atraso = (hoje - data_devolucao).days
                    
                    tree2.insert("", "end", values=(
                        emprestimo['cod_emprestimo'],
                        livro_titulo,
                        aluno_nome,
                        emprestimo['data_devolucao'],
                        dias_atraso
                    ))
        
        # Consulta 3: Quantidade de empréstimos por período
        frame_consulta3 = ttk.Frame(notebook_consultas)
        notebook_consultas.add(frame_consulta3, text="Empréstimos por Período")
        
        ttk.Label(frame_consulta3, text="Data Inicial (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_data_inicio = ttk.Entry(frame_consulta3)
        entry_data_inicio.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame_consulta3, text="Data Final (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_data_fim = ttk.Entry(frame_consulta3)
        entry_data_fim.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        lbl_resultado = ttk.Label(frame_consulta3, text="")
        lbl_resultado.grid(row=2, column=0, columnspan=2, pady=5)
        
        btn_calcular = ttk.Button(frame_consulta3, text="Calcular", command=lambda: self.calcular_emprestimos_periodo(
            entry_data_inicio.get(), entry_data_fim.get(), lbl_resultado))
        btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)
    
    def calcular_emprestimos_periodo(self, data_inicio, data_fim, lbl_resultado):
        if not data_inicio or not data_fim:
            messagebox.showerror("Erro", "Ambas as datas são obrigatórias!")
            return
        
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use YYYY-MM-DD.")
            return
        
        quantidade = 0
        for emprestimo in self.tabelas['emprestimos']:
            data_emprestimo = datetime.strptime(emprestimo['data_emprestimo'], '%Y-%m-%d')
            if data_inicio <= data_emprestimo <= data_fim:
                quantidade += 1
        
        lbl_resultado.config(text=f"Quantidade de empréstimos no período: {quantidade}")
    
    def excluir_registro(self, tree, tabela, chave_primaria):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum registro selecionado!")
            return
        
        item = selecionado[0]
        valores = tree.item(item, "values")
        chave = valores[0]  # Assumindo que a chave primária é a primeira coluna
        
        # Confirmar exclusão
        if not messagebox.askyesno("Confirmar", f"Deseja excluir o registro {chave}?"):
            return
        
        # Marcar como inativo
        for i, registro in enumerate(self.tabelas[tabela]):
            if registro[chave_primaria] == chave:
                self.tabelas[tabela][i]['ativo'] = '0'
                break
        
        # Salvar tabela
        colunas = {
            'cidades': ['codigo', 'descricao', 'estado', 'ativo'],
            'cursos': ['codigo', 'descricao', 'ativo'],
            'alunos': ['cod_aluno', 'nome', 'cod_curso', 'cod_cidade', 'ativo'],
            'autores': ['cod_autor', 'nome', 'cod_cidade', 'ativo'],
            'categorias': ['cod_categoria', 'descricao', 'ativo'],
            'livros': ['cod_livro', 'titulo', 'cod_autor', 'cod_categoria', 'ano_publicacao', 'disponibilidade', 'ativo'],
            'emprestimos': ['cod_emprestimo', 'cod_livro', 'cod_aluno', 'data_emprestimo', 'data_devolucao', 'devolvido', 'ativo']
        }
        
        self.salvar_tabela(f'{tabela}.csv', self.tabelas[tabela], colunas[tabela])
        
        # Atualizar a visualização
        tree.delete(item)
        messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
    
    def recarregar_aba(self, aba):
        # Recarregar dados da tabela
        self.tabelas[aba] = self.carregar_tabela(f'{aba}.csv')
        
        # Recriar a aba
        if aba == 'cidades':
            self.configurar_aba_cidades()
        elif aba == 'cursos':
            self.configurar_aba_cursos()
        elif aba == 'alunos':
            self.configurar_aba_alunos()
        elif aba == 'autores':
            self.configurar_aba_autores()
        elif aba == 'categorias':
            self.configurar_aba_categorias()
        elif aba == 'livros':
            self.configurar_aba_livros()
        elif aba == 'emprestimos':
            self.configurar_aba_emprestimos()
        elif aba == 'devolucoes':
            self.configurar_aba_devolucoes()
        elif aba == 'consultas':
            self.configurar_aba_consultas()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaFrontend(root)
    root.mainloop()