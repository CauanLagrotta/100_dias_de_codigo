from tkinter import *

# Cores
preto = "#000000" 
branco = "#ffffff" 
cinza = "#eceff1"
vermelho = "#ff5722"
cinza_escuro = "#363636"
roxo = "#7E00D1"

#Criando a janela
janela = Tk()
janela.title("Calculando °C em °F")
janela.geometry("350x340")
janela.config(bg=cinza_escuro)

# Criando bordas inferiores
def Bordas():
    canvas = Canvas(janela, width=180, height=2, background=cinza_escuro, highlightthickness=0)
    canvas.create_line(0, 2, 180, 2, fill=branco, width=2)
    canvas.pack(pady=3)

def Calcular():
    try:
        c = int(entry_n1.get())
        f = c * 1.8 + 32
        resultado.config(text=f'{f} °F')
      
    except ValueError:
        resultado.config(text='Insira apenas números válidos',  fg=vermelho)

# Titulo
label_titulo = Label(janela, text="Convertendo °C em °F", font=('Arial bold', 20), background=cinza_escuro, fg=roxo)
label_titulo.pack(pady=20)

# Criando os frames 
#Numero

label_n1 = Label(janela, text="Temperatura em °C: ", font=('Arial', 12), background=cinza_escuro, fg=branco)
label_n1.pack(pady=10)

entry_n1 = Entry(janela, font=('Arial', 12), relief=FLAT, width=15, background=cinza_escuro, fg=branco, border=1 )
entry_n1.pack(pady=5)

Bordas()

botaoCalcular = Button(janela, text="Calcular", command=Calcular, font=('Arial', 12), relief=FLAT, width=15, background=roxo, fg=branco, border=1 )
botaoCalcular.pack(pady=15)

resultado = Label(janela, text="Resultado em °F: ", font=('Arial bold', 18), background=cinza_escuro, fg=roxo)
resultado.pack(pady=20)


janela.mainloop()

# c = int(input('Insira um número: '))

# f = c * 1.8 + 32

# print(f)