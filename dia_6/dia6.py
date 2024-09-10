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

def Calcular():
    try:
        n1 = int(entry_n1.get())
        fatorial = 1
        
        for i in range(1, n1+1):
            fatorial *= i
            resultado.config(text = f'Fatorial: {fatorial}')
        
    except ValueError:
        resultado.config(text='Insira apenas números válidos',  fg=vermelho)

# Criando a janela
janela = Tk()
janela.title("Calculadora Fatorial")
janela.geometry("350x340")
janela.config(bg=cinza_escuro)

# Titulo
label_titulo = Label(janela, text="Calculadora Fatorial", font=('Arial bold', 20), background=cinza_escuro, fg=roxo)
label_titulo.pack(pady=20)

# Criando Frames
#Numero
label_n1 = Label(janela, text="Insira um número: ", font=('Arial', 12), background=cinza_escuro, fg=branco)
label_n1.pack(pady=10)

entry_n1 = Entry(janela, font=('Arial', 12), relief=FLAT, width=15, background=cinza_escuro, fg=branco, border=1 )
entry_n1.pack(pady=5)

Bordas()

botaoCalcular = Button(janela, text="Calcular", command=Calcular, font=('Arial', 12), relief=FLAT, width=15, background=roxo, fg=branco, border=1 )
botaoCalcular = botaoCalcular.pack(pady=15)

resultado = Label(janela, text="Resultado: ", font=('Arial bold', 18), background=cinza_escuro, fg=roxo)
resultado.pack(pady=10)


janela.mainloop()

# n = int(input('Insira um número: '))

# fatorial = 1

# for i in range(1, n + 1):
#     fatorial *= i

# print(fatorial)