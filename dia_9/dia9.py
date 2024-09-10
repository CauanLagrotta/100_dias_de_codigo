from tkinter import *
from tkinter import ttk  
import pandas as pd
import numpy as np

# Cores
preto = "#000000" 
branco = "#ffffff" 
cinza = "#eceff1"
vermelho = "#ff5722"
cinza_escuro = "#363636"
roxo = "#7E00D1"

# Criando a janela
janela = Tk()
janela.title("Tabela De Vendas")
janela.geometry("800x600")
janela.config(bg=cinza_escuro)

# Criando a Tabela
def CriarTabelaProdutos():
    limparTabela()
    
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview", background=cinza_escuro, foreground=branco, rowheight=25, fieldbackground=cinza_escuro)
    estilo.configure("Treeview.Heading", background=roxo, foreground=branco)
    
    estilo.map("Treeview", bg=[("selected", roxo)], fg=[("selected", branco)])
    
    # Criando a tabela
    tabela['columns'] = ('Produtos', 'Vendas', 'Custo')
    
    # Definindo os cabeçalhos
    tabela.heading('Produtos', text='Produtos')
    tabela.heading('Vendas', text='Vendas')
    tabela.heading('Custo', text='Custo')
    
    # Ajustando o tamanho das colunas
    tabela.column('Produtos', width=200, anchor=CENTER)
    tabela.column('Vendas', width=150, anchor=CENTER)
    tabela.column('Custo', width=150, anchor=CENTER)

    
    # Inserindo os dados na tabela
    produtos = [
        ('Camisa', 1102, 'R$ 125,00'),
        ('Calça', 938, 'R$ 65,00'),
        ('Tenis', 918, 'R$ 300,00')
    ]
    
    for produto in produtos:
        tabela.insert('', 'end', values=produto)
        

# Função para calcular e exibir as estatísticas
def CriarTabelaEstatisticas():
    limparTabela()
    
    df = pd.DataFrame({
        'Vendas': np.random.randint(50, 100, size=10)
    })
   
    media = df['Vendas'].mean()
    mediana = df['Vendas'].median()
    desvio_padrao = df['Vendas'].std()
    maximo = df['Vendas'].max()
    minimo = df['Vendas'].min()
    
    # Estilo
    estilo = ttk.Style()
    estilo.theme_use("clam")
    
    estilo.configure("Treeview", background=cinza_escuro, fg=branco, rowheight=25, fieldbackground=cinza_escuro)
    estilo.configure("Treeview.Heading", background=roxo, fg=branco)
    estilo.map("Treeview", background=[("selected", roxo)], foreground=[("selected", branco)])
    
    # Tabela estatisticas
    tabela['columns'] = ('Estatisticas', 'Valores')
    
    tabela.heading('Estatisticas', text='Estatisticas')
    tabela.heading('Valores', text='Valores')
    
    tabela.column('Estatisticas', width=200, anchor=CENTER)
    tabela.column('Valores', width=150, anchor=CENTER)
    
    # Enviando dados pra tabela
    estatisticas = [
        ('Media', f"{media:.2f}"),	
        ('Mediana', f"{mediana:.2f}"),
        ('Desvio Padrao', f"{desvio_padrao:.2f}"),
        ('Maximo', f"{maximo:.2f}"),
        ('Minimo', f"{minimo:.2f}"),
    ]
    
    for est in estatisticas:
        tabela.insert('', 'end', values=est)
        
# Função limpar tabela 

def limparTabela():
    for row in tabela.get_children():
        tabela.delete(row)

# Adicionar item

def adicionarItem():
    limparTabela()
    
    def salvarItem():
        produto = entryProdutos.get()
        vendas = entryVendas.get()
        custo = entryCusto.get()
        
        if produto and vendas and custo:
            tabela.insert('', 'end', values=(produto, vendas, custo))
            adicionarJanela.destroy()
            

    # janela pora adicionar items
    adicionarJanela = Toplevel()
    adicionarJanela.title("Adicionar Item")
    adicionarJanela.geometry("400x400")
    adicionarJanela.config(bg=cinza_escuro)

    Label(adicionarJanela, text="Produto: ", bg=cinza_escuro, fg=branco).pack(pady=10)
    entryProdutos = Entry(adicionarJanela)
    entryProdutos.pack(pady=5)

    Label(adicionarJanela, text="Vendas: ", bg=cinza_escuro, fg=branco).pack(pady=10)
    entryVendas = Entry(adicionarJanela)
    entryVendas.pack(pady=5)

    Label(adicionarJanela, text="Custo: ", bg=cinza_escuro, fg=branco).pack(pady=10)
    entryCusto = Entry(adicionarJanela)
    entryCusto.pack(pady=5)

    Button(adicionarJanela, text="Salvar", command=salvarItem, bg=roxo, fg=branco).pack(pady=10)


# Tabela
tabela = ttk.Treeview(janela, show='headings')
tabela.pack(pady=20, fill=BOTH, expand=True)

# Frame para os botoes
frameBotoes = Frame(janela, bg=cinza_escuro)
frameBotoes.pack(pady=20, fill=X)

# Botoes
botaoProdutos = Button(frameBotoes, text="Tabela De Produtos", command=CriarTabelaProdutos, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1 )
botaoProdutos.grid(row=0, column=0, padx=10)

botaoEstatisticas = Button(frameBotoes, text="Estatisticas", command=CriarTabelaEstatisticas, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1 )
botaoEstatisticas.grid(row=0, column=1, padx=10)

botaoAdicionarItems = Button(frameBotoes, text="Adicionar Items", command=adicionarItem, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1 )
botaoAdicionarItems.grid(row=0, column=2, padx=10)


CriarTabelaProdutos()
janela.mainloop()
