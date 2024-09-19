import csv
import os
from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np

# Cores
preto = "#000000"
branco = "#ffffff"
cinza = "#eceff1"
vermelho = "#ff5722"
cinza_escuro = "#363636"
roxo = "#7E00D1"

# Armazenar salários
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(diretorio_atual, "salario.csv")

salarios = []

def carregarSalarios():
    global salarios
    
    try:
        with open(arquivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            salarios = [[row[0], float(row[1])] for row in reader]
    
    except FileNotFoundError:
        salarios = []

def salvarSalarios():
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(salarios)

# Criando a janela principal
janela = Tk()
janela.title("Tabela De Salários")
janela.geometry("800x600")
janela.config(bg=cinza_escuro)

# Criando a Tabela de Salários
def CriarTabelaSalarios():
    limparTabela()
    
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview", background=cinza_escuro, foreground=branco, rowheight=25, fieldbackground=cinza_escuro)
    estilo.configure("Treeview.Heading", background=roxo, foreground=branco)
    
    estilo.map("Treeview", bg=[("selected", roxo)], fg=[("selected", branco)])
    
    # Criando a tabela
    tabela['columns'] = ('Nome', 'Salario')
    
    # Definindo os cabeçalhos
    tabela.heading('Nome', text='Nome')
    tabela.heading('Salario', text='Salario')
    
    # Definindo as colunas
    tabela.column('Nome', anchor=CENTER, width=200)
    tabela.column('Salario', anchor=CENTER, width=150)
    
    # Inserindo os dados na tabela
    for salario in salarios:
        tabela.insert('', 'end', values=(salario[0], f'{salario[1]:.2f}'))

# Limpar tabela
def limparTabela():
    for row in tabela.get_children():
        tabela.delete(row)

# Adicionar novo item (salário)
def adicionarItem():
    def salvarItem():
        nome = entryNome.get()
        salario = entrySalario.get()
        
        if nome and salario:
            try:
                nome = str(nome)
                salario = float(salario)
                
                salarios.append([nome, salario])
                
                salvarSalarios()
                
                CriarTabelaSalarios()  # Atualizar a tabela
                adicionarJanela.destroy()  # Fechar a janela após salvar
            
            except ValueError:
                messagebox.showerror("Erro", "Insira um número válido no campo Salário")
            
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")
    
    # Janela para adicionar item
    adicionarJanela = Toplevel()
    adicionarJanela.title("Adicionar Item")
    adicionarJanela.geometry("400x400")
    adicionarJanela.config(bg=cinza_escuro)
    
    Label(adicionarJanela, text="Nome", bg=cinza_escuro, fg=branco).pack(pady=10)
    entryNome = Entry(adicionarJanela)
    entryNome.pack(pady=5)
    
    Label(adicionarJanela, text="Salario: ", bg=cinza_escuro, fg=branco).pack(pady=10)
    entrySalario = Entry(adicionarJanela)
    entrySalario.pack(pady=5)

    Button(adicionarJanela, text="Salvar", command=salvarItem, bg=roxo, fg=branco).pack(pady=10)

# Mostrar estatísticas (média, máximo, mínimo)
def mostrarEstatisticas():
    if len(salarios) == 0:
        messagebox.showwarning("Aviso", "Nenhum dado disponível")
        return
    
    # Calculando estatísticas
    salarios_numeros = [salario[1] for salario in salarios]
    media_salario = np.mean(salarios_numeros)
    salario_max = np.max(salarios_numeros)
    salario_min = np.min(salarios_numeros)
    total_funcionarios = len(salarios)
    
    # Janela de Estatísticas
    estatisticasJanela = Toplevel()
    estatisticasJanela.title("Estatísticas")
    estatisticasJanela.geometry("400x400")
    estatisticasJanela.config(bg=cinza_escuro)
    
    Label(estatisticasJanela, text=f"Média Salarial: R${media_salario:.2f}", bg=cinza_escuro, fg=branco).pack(pady=10)
    Label(estatisticasJanela, text=f"Salário Máximo: R${salario_max:.2f}", bg=cinza_escuro, fg=branco).pack(pady=10)
    Label(estatisticasJanela, text=f"Salário Mínimo: R${salario_min:.2f}", bg=cinza_escuro, fg=branco).pack(pady=10)
    Label(estatisticasJanela, text=f"Total de Funcionários: {total_funcionarios}", bg=cinza_escuro, fg=branco).pack(pady=10)

# Tabela
tabela = ttk.Treeview(janela, show='headings')
tabela.pack(pady=20, fill=BOTH, expand=True)

# Frame para os botões
frameBotoes = Frame(janela, bg=cinza_escuro)
frameBotoes.pack(pady=20, fill=X)

# Botões
botaoSalarios = Button(frameBotoes, text="Tabela De Salarios", command=CriarTabelaSalarios, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1)
botaoSalarios.grid(row=0, column=0, padx=10)

botaoAdicionarItems = Button(frameBotoes, text="Adicionar Items", command=adicionarItem, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1)
botaoAdicionarItems.grid(row=0, column=1, padx=10)

# Novo botão para estatísticas
botaoEstatisticas = Button(frameBotoes, text="Ver Estatísticas", command=mostrarEstatisticas, font=('Arial', 12), relief=FLAT, width=20, background=roxo, fg=branco, border=1)
botaoEstatisticas.grid(row=0, column=2, padx=10)

carregarSalarios()
CriarTabelaSalarios()
janela.mainloop()
