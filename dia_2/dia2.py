from tkinter import *
from tkinter import ttk

# Cores
preto = "#000000" 
branco = "#ffffff" 
cinza = "#eceff1"
vermelho = "#ff5722"
cinza_escuro = "#363636"
roxo = "#7E00D1"

# Criando bordas inferiores
def Bordas():
    canvas = Canvas(janela, width=180, height=2, background=cinza_escuro, highlightthickness=0)
    canvas.create_line(0, 2, 180, 2, fill=branco, width=2)
    canvas.pack(pady=3)
    
# Função para calcular soma
def calcular_soma():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())

        soma = n1 + n2
        
        resultado.config(text = f'Soma: {soma}')
   
    except ValueError:
        resultado.config(text='Insira apenas números válidos',  fg=vermelho)


# Criando a janela
janela = Tk()
janela.title("Soma de dois Numeros")
janela.geometry("350x380")
janela.config(bg=cinza_escuro)


# Titulo
label_titulo = Label(janela, text="Soma de dois Numeros", font=('Arial bold', 20), background=cinza_escuro, fg=roxo)
label_titulo.pack(pady=20)

# Criando os frames
# Numero 1
label_n1 = Label(janela, text="Primeiro numero: ", font=('Arial', 12), background=cinza_escuro, fg=branco)
label_n1.pack(pady=10)

entry_n1 = Entry(janela, font=('Arial', 12), relief=FLAT, width=15, background=cinza_escuro, fg=branco, border=1 )
entry_n1.pack(pady=5)

Bordas()

# Numero 2
label_n2 = Label(janela, text="Segundo numero: ", font=('Arial', 12), background=cinza_escuro, fg=branco)
label_n2.pack(pady=10)

entry_n2 = Entry(janela, font=('Arial', 12), relief=FLAT, width=15, background=cinza_escuro, fg=branco, border=1 )
entry_n2.pack(pady=5)

Bordas()


botaoCalcular = Button(janela, text="Calcular", command=calcular_soma, font=('Arial', 12), relief=FLAT, width=15, background=roxo, fg=branco, border=1 )
botaoCalcular.pack(pady=15)


resultado = Label(janela, text="Soma: ", font=('Arial bold', 18), background=cinza_escuro, fg=roxo)
resultado.pack(pady=10)

janela.mainloop()