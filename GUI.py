import numpy as np
from PIL import Image, ImageTk
from casamento import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import tkinter as tk
from tkinter import RIGHT, Button, ttk

casamento = Casamento(zo=50,zl=10,freq=10000,l_linha=10,amplitude=15)

# root window
root = tk.Tk()

# Adquirir tamanho da tela do usupario
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width=screen_width-650
heigth=screen_height-250
root.geometry(f"{width}x{heigth}")

# root.geometry('800x600')
root.configure(bg="white")
root.title('Casamento de Impedâncias')

# Criando um notebook do tk
notebook = ttk.Notebook(root, height= screen_height, width=screen_width)
notebook.pack(pady=0, expand=False)

# Abas (frames) de menu e dos casamentos

style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("dark.TFrame", background="black")

frame1 = ttk.Frame(notebook, width=800 , height=600, style="TFrame")
frame2 = ttk.Frame(notebook, width=800 , height=600)
frame3 = ttk.Frame(notebook, width=800 , height=600)
frame4 = ttk.Frame(notebook, width=800 , height=600)


frame1.pack(fill='both', expand=True)  # Menu
frame2.pack(fill='both', expand=True)  # Gerador Excitação independente
frame3.pack(fill='both', expand=True)  # Gerador Shunt
frame4.pack(fill='both', expand=True)  # Gerador Série


notebook.add(frame1, text='Menu')
notebook.add(frame2, text='Casamento Série')
notebook.add(frame3, text='Stub em curto')
notebook.add(frame4, text='Stub aberto')


# Menu

## Foto da linha de transmissão
img_menu = ImageTk.PhotoImage(Image.open("Imagens/menu3.png"))
texto_menu = tk.Label(frame1, image=img_menu)
texto_menu.grid(row = 0, column = 0, columnspan=3,pady=20, padx=20, sticky="WE")

## Label onde serão inseriadas as variáveis
variaveis = tk.LabelFrame(frame1, text= "Insira aqui as variáveis: ", padx=50, pady=8)
variaveis.grid(row = 1, column=0, padx=20)

# Variáveis
label_zo = tk.Label(variaveis,text='Impedância Característica(Ohm):').grid(row=0, column=0)
caixa_zo = tk.Entry(variaveis, width=7)
caixa_zo.insert(0, 50)
caixa_zo.grid(row=0, column=1)

label_zl = tk.Label(variaveis,text='Impedância da carga(Ohm):').grid(row=1, column=0)
caixa_zl = tk.Entry(variaveis, width=7)
caixa_zl.insert(0, 10)
caixa_zl.grid(row=1, column=1)

label_freq = tk.Label(variaveis,text='Frequência de excitação(MHz):').grid(row=2, column=0)
caixa_freq = tk.Entry(variaveis, width=7)
caixa_freq.insert(0, 100)
caixa_freq.grid(row=2, column=1)

label_l = tk.Label(variaveis,text='Comprimento da linha(m):').grid(row=4, column=0)
caixa_l = tk.Entry(variaveis, width=7)
caixa_l.insert(0, 10)
caixa_l.grid(row=4, column=1)

label_amp = tk.Label(variaveis,text='Amplitude do gerador(Volts):').grid(row=5, column=0)
caixa_amp = tk.Entry(variaveis, width=7)
caixa_amp.insert(0, 15)
caixa_amp.grid(row=5, column=1)

# Botões do menu

#Comando do save
def salvar():
    casamento.zo=float(caixa_zo.get())
    casamento.zl=float(caixa_zl.get())
    casamento.freq=float(caixa_freq.get())
    casamento.l_linha=float(caixa_l.get())
    casamento.amplitude=float(caixa_amp.get())
    
# Salvar os valores atuais
button_salvar = tk.Button(frame1, text='Salvar valores', command= salvar(), pady=10)
button_salvar.grid(pady=10, row = 1, column = 2)

# Modo escuro
#Comando do modo escuro
def toggle_theme():
    current_bg = frame1.cget("style")  # Obter o estilo atual

    # Alternar entre os modos escuro e claro
    if current_bg == "TFrame":
        new_bg = "dark.TFrame"
    else:
        new_bg = "TFrame"

    # Atualizar o estilo do frame
    frame1.configure(style=new_bg)
    frame2.configure(style=new_bg)
    frame3.configure(style=new_bg)
    frame4.configure(style=new_bg)

button_mudar_tema = tk.Button(frame1, text="Alternar Tema", command=toggle_theme)
button_mudar_tema.grid(pady=10, row = 0, column = 4)

# Botões para mudar de aba

#Comando dos botões de troca de aba
def mudar_tab(notebook, tab_destino):
    Tabs = notebook
    Tabs.select(tab_destino)
    
botoes_menu = tk.LabelFrame(frame1, padx=30, pady=10, border=0)
botoes_menu.grid(row = 1, column=3, sticky="E")

botao_serie = tk.Button(botoes_menu, text='Casamento Série', command=lambda:mudar_tab(notebook, frame2))
botao_serie.grid(row=0, pady=10, sticky="WE")

botao_curto = tk.Button(botoes_menu, text='Stub em curto', command=lambda:mudar_tab(notebook, frame3))
botao_curto.grid(row=1, pady=10, sticky="WE")

botao_aberto = tk.Button(botoes_menu, text='Stub aberto', command=lambda:mudar_tab(notebook, frame4))
botao_aberto.grid(row=2, pady=10, sticky="WE")



#Botões de voltar para o menu a partir das abas de casamento, usando o comando mudar_tab
botao_menu_1 = tk.Button(frame2, text = "Voltar",width=16, height=2,  command = lambda:mudar_tab(notebook, frame1))
botao_menu_1.grid(row=0,column=3)

botao_menu_2 = tk.Button(frame3, text = "Voltar",width=16, height=2,  command = lambda:mudar_tab(notebook, frame1))
botao_menu_2.grid(row=0,column=3)

botao_menu_3 = tk.Button(frame4, text = "Voltar",width=16, height=2,  command = lambda:mudar_tab(notebook, frame1))
botao_menu_3.grid(row=0,column=3)

#Comandos para simular
def simular_serie(casamento):
    zo = casamento.zo
    zl = casamento.zl
    freq = casamento.freq
    l_linha = casamento.l_linha
    amplitude = casamento.amplitude
    x = np.linspace(0, l_linha,1000)

    casamento_serie = Serie(zo=zo, zl=zl,freq=freq,l_linha = l_linha, amplitude = amplitude)
    x1, dist = casamento_serie.simular()
    
    V = amplitude * np.cos(2*np.pi*freq * (l_linha-x)/300) + amplitude * np.cos(-2*np.pi*freq * (l_linha-x)/300)
    
    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame2, padx=10, pady=10, border=0)
    frame_grafico.grid(row=3,column=1, columnspan=3)
    
    fig = Figure(figsize = (4.0, 3.0), dpi = 100)
    
    subplot = fig.add_subplot(1, 1, 1)
    
# Plotar a curva estacionária
    subplot.plot(x, V)
    subplot.plot(x, -1*V)

# Configurações do gráfico
    subplot.set_title("Padrão estacionário de tensão na linha")
    subplot.set_ylim(-2*amplitude, 2*amplitude)
    subplot.set_xlabel('Distância do gerador (m)')
    subplot.set_ylabel('Tensão (V)')
    subplot.legend()
    subplot.grid(True)

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()
        
    #inserindo resultados nos labels 
    caixa_reatancia_serie.insert(0, x1)
    caixa_distancia_serie.insert(0, dist)

def simular_curto(casamento):
    zo = casamento.zo
    zl = casamento.zl
    freq = casamento.freq
    l_linha = casamento.l_linha
    amplitude = casamento.amplitude
    x = np.linspace(0, l_linha,1000)

    casamento_curto = Curto(zo=zo, zl=zl,freq=freq,l_linha = l_linha, amplitude = amplitude)
    dist, l = casamento_curto.simular()
    
    V = amplitude * np.cos(2*np.pi*freq * (l_linha-x)/300) + amplitude * np.cos(-2*np.pi*freq * (l_linha-x)/300)
    
    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame3, padx=10, pady=10, border=0)
    frame_grafico.grid(row=3,column=1, columnspan=3)
    
    fig = Figure(figsize = (4.0, 3.0), dpi = 100)
    
    subplot = fig.add_subplot(1, 1, 1)
  
# Plotar a curva estacionaria
    subplot.plot(x, V)
    subplot.plot(x, -1*V)

# Configurações do gráfico
    subplot.set_title("Padrão estacionário de tensão na linha")
    subplot.set_ylim(-2*amplitude, 2*amplitude)
    subplot.set_xlabel('Distância do gerador (m)')
    subplot.set_ylabel('Tensão (V)')
    subplot.legend()
    subplot.grid(True)

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()
        
    #inserindo resultados nos labels 
    caixa_distancia_curto.insert(0, dist*100)
    caixa_comprimento_curto.insert(0, l*100)


def simular_aberto(casamento):
    zo = casamento.zo
    zl = casamento.zl
    freq = casamento.freq
    l_linha = casamento.l_linha
    amplitude = casamento.amplitude
    x = np.linspace(0, l_linha,1000)


    casamento_aberto = Aberto(zo=zo, zl=zl,freq=freq,l_linha = l_linha, amplitude = amplitude)
    dist, l = casamento_aberto.simular()
    
    V = amplitude * np.cos(2*np.pi*freq * (l_linha-x)/300) + amplitude * np.cos(-2*np.pi*freq * (l_linha-x)/300)
    
    # Frame para colocar o grafico
    frame_grafico = tk.LabelFrame(frame4, padx=10, pady=10, border=0)
    frame_grafico.grid(row=3,column=1, columnspan=3)
    
    fig = Figure(figsize = (4.0, 3.0), dpi = 100)
    
    subplot = fig.add_subplot(1, 1, 1)
       
# Plotar a curva estacionaria
    subplot.plot(x, V)
    subplot.plot(x, -1*V)

# Configurações do gráfico
    subplot.set_title("Padrão estacionário de tensão na linha")
    subplot.set_ylim(-2*amplitude, 2*amplitude)
    subplot.set_xlabel('Distância do gerador (m)')
    subplot.set_ylabel('Tensão (V)')
    subplot.legend()
    subplot.grid(True)

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()
        
    #inserindo resultados nos labels 
    caixa_distancia_aberto.insert(0, dist*100)
    caixa_comprimento_aberto.insert(0, l*100)
    
#Botões de simular
button_serie = tk.Button(frame2, width=16, height=2, text='Simular', command = lambda:simular_serie(casamento))
button_serie.grid(row=0, column=1, padx=80)

button_curto = tk.Button(frame3, width=16, height=2, text='Simular', command = lambda:simular_curto(casamento))
button_curto.grid(row=0, column=1, padx=80)

button_aberto = tk.Button(frame4, width=16, height=2, text='Simular', command = lambda:simular_aberto(casamento))
button_aberto.grid(row=0, column=1, padx=80)

# Labels para mostrar o resultado em cada aba de casamento
resultados_serie = tk.LabelFrame(frame2, text= "Resultados: ", padx=50, pady=10)
resultados_serie.grid(row = 2, column=1, padx=20)

label_reatancia_serie = tk.Label(resultados_serie,text='Reatância da Carga (Ohm):').grid(row=1, column=0)
caixa_reatancia_serie = tk.Entry(resultados_serie, width=7)
caixa_reatancia_serie.insert(0, 0)
caixa_reatancia_serie.grid(row=1, column=1)


label_distancia_serie = tk.Label(resultados_serie,text='Distancia da carga à reatância (m):').grid(row=2, column=0)
caixa_distancia_serie = tk.Entry(resultados_serie, width=7)
caixa_distancia_serie.insert(0, 0)
caixa_distancia_serie.grid(row=2, column=1)


resultados_curto = tk.LabelFrame(frame3, text= "Resultados: ", padx=50, pady=10)
resultados_curto.grid(row = 2, column=1, padx=20)

label_distancia_curto = tk.Label(resultados_curto,text='Distância do stub à carga(cm):').grid(row=1, column=0)
caixa_distancia_curto = tk.Entry(resultados_curto, width=7)
caixa_distancia_curto.insert(0, 0)
caixa_distancia_curto.grid(row=1, column=1)


label_comprimento_curto = tk.Label(resultados_curto,text='Comprimento do stub (cm):').grid(row=2, column=0)
caixa_comprimento_curto = tk.Entry(resultados_curto, width=7)
caixa_comprimento_curto.insert(0, 0)
caixa_comprimento_curto.grid(row=2, column=1)

resultados_aberto = tk.LabelFrame(frame4, text= "Resultados: ", padx=50, pady=10)
resultados_aberto.grid(row = 2, column=1, padx=20)

label_distancia_aberto = tk.Label(resultados_aberto,text='Distância do stub à carga(cm):').grid(row=1, column=0)
caixa_distancia_aberto = tk.Entry(resultados_aberto, width=7)
caixa_distancia_aberto.insert(0, 0)
caixa_distancia_aberto.grid(row=1, column=1)

label_comprimento_aberto = tk.Label(resultados_aberto,text='Comprimento do stub (cm):').grid(row=2, column=0)
caixa_comprimento_aberto = tk.Entry(resultados_aberto, width=7)
caixa_comprimento_aberto.insert(0, 0)
caixa_comprimento_aberto.grid(row=2, column=1)

root.mainloop()


