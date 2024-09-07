#Criando uma calculadora

from tkinter import *
from tkinter import ttk

preto = "#000000" 
branco = "#ffffff" 
cinza = "#eceff1"
vermelho = "#ff5722"
cinza_escuro = "#363636"
roxo = "#7E00D1"

 # Configurando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=preto)

# Criando os frames
frame_tela = Frame(janela, width=235, height=50, bg=preto)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=preto)
frame_corpo.grid(row=1, column=0)

todos_valores = ''      

#Funcao entrada valor
def entrada_valor(event):
    global todos_valores
    
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


# Funcao calcular
def calcular():
    global todos_valores
    
    if '%' in todos_valores:
        valores = todos_valores.split('%')
        resultado = float(valores[0]) * (float(valores[1]) / 100)
        
    else: 
        resultado = eval(todos_valores)
        
    valor_texto.set(str(resultado))
    
# Funcao limpar
def limpar():
    global todos_valores
    
    todos_valores = ''
    valor_texto.set('')


# Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2,  relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=preto, fg=branco)
app_label.place(x=0, y=0)



# Criando os botoes
# LINHA 1
b_limpar = Button(frame_corpo, text="C", command=limpar, width=11, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=vermelho, relief=RAISED, overrelief=RIDGE)
b_limpar.place(x=0, y=0)

b_porcentagem = Button(frame_corpo, command = lambda: entrada_valor('%'), text="%", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_porcentagem.place(x=118, y=0)

b_divisao = Button(frame_corpo, command=lambda: entrada_valor('/'), text="/", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=roxo, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)

# LINHA 2
b_7 = Button(frame_corpo, command=lambda: entrada_valor('7'), text="7", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)

b_8 = Button(frame_corpo, command=lambda: entrada_valor('8'), text="8", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)

b_9 = Button(frame_corpo, command=lambda: entrada_valor('9'), text="9", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)

b_multiplicacao = Button(frame_corpo, command=lambda: entrada_valor('*'), text="*", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=roxo, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_multiplicacao.place(x=177, y=52)

# LINHA 3
b_4 = Button(frame_corpo, command=lambda: entrada_valor('4'), text="4", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)

b_5 = Button(frame_corpo, command=lambda: entrada_valor('5'), text="5", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)

b_6 = Button(frame_corpo, command=lambda: entrada_valor('6'),text="6", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)

b_subtracao = Button(frame_corpo, command=lambda: entrada_valor('-'), text="-", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=roxo, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_subtracao.place(x=177, y=104)

# LINHA 4
b_1 = Button(frame_corpo, text="1", command=lambda: entrada_valor('1'), width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)

b_2 = Button(frame_corpo, text="2", command=lambda: entrada_valor('2'),width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)

b_3 = Button(frame_corpo, text="3", command=lambda: entrada_valor('3'),width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)

b_adicao = Button(frame_corpo, text="+", command=lambda: entrada_valor('+'), width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=roxo, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_adicao.place(x=177, y=156)

# LINHA 5
b_0 = Button(frame_corpo, text="0", command=lambda: entrada_valor('0'), width=11, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)

b_ponto = Button(frame_corpo, text=".", command=lambda: entrada_valor('.'), width=5, height=2, bg=cinza, font=('Ivy 13 bold'), background=cinza_escuro, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=208)

b_igual = Button(frame_corpo, text="=", command=calcular, width=5, height=2, font=('Ivy 13 bold'), background=roxo, bd=0, fg=branco, relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=208)




janela.mainloop()