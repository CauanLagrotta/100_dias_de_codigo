import tkinter as tk

def interpolate_color(color1, color2, factor):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    
    return f'#{r:02x}{g:02x}{b:02x}'

def fade_text(fade_in = True):
    global fade_factor, fade_step
    
    #Cores de inicio e fim
    cor_inicio = '#7E00D1'
    cor_fim = '#307BE8'
    
    # Calcular a cor intermediaria
    cor_atual = interpolate_color(cor_inicio, cor_fim, fade_factor)
    label.config(fg = cor_atual)
    
    # Atualizar o fator de fade
    if fade_in:
        if fade_factor < 1.0:
            fade_factor += fade_step
        
        else:
            janela.after(1000, lambda: fade_text(fade_in=False))
            return
        
    else:
        if fade_factor > 0.0:
            fade_factor -= fade_step
            
        else:
            janela.after(1000, lambda: fade_text(fade_in=True))
            return
        
    janela.after(30, lambda: fade_text(fade_in=fade_in))
    

# Criando a janela
janela = tk.Tk()
janela.title("Hello World")
janela.geometry("500x500")
janela.config(bg='#363636')
    

# Label 
fade_factor = 0.0
fade_step = 0.01
label = tk.Label(janela, text="Hello World", font=("Arial", 40), bg='#363636')
label.pack(expand=True)

#Efeito de fade in
fade_text(fade_in=True)

janela.mainloop()
    