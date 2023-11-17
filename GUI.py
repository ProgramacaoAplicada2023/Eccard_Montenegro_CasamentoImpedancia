import numpy as np
from PIL import Image, ImageTk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import tkinter as tk
from tkinter import RIGHT, Button, ttk
import math

# Função a ser aplicada nos botões
def mudar_tab(notebook, tab_destino):
    Tabs = notebook
    Tabs.select(tab_destino)
    

# root window
root = tk.Tk()

# Tamanho da tela do usuário
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width=screen_width-650
heigth=screen_height-250
root.geometry(f"{width}x{heigth}")

# root.geometry('800x600')
root.configure(bg="white")
root.title('Casa Impedância')


# Notebook para manusear diferentes abas)
notebook = ttk.Notebook(root, height= screen_height, width=screen_width)
notebook.pack(pady=0, expand=False)

# Criando as abas
frame1 = ttk.Frame(notebook, width=800 , height=600)
frame2 = ttk.Frame(notebook, width=800 , height=600)
frame3 = ttk.Frame(notebook, width=800 , height=600)
frame4 = ttk.Frame(notebook, width=800 , height=600)
frame5 = ttk.Frame(notebook, width=800 , height=600)

frame1.pack(fill='both', expand=True)  # Menu
frame2.pack(fill='both', expand=True)  # Gerador Excitação independente
frame3.pack(fill='both', expand=True)  # Gerador Shunt
frame4.pack(fill='both', expand=True)  # Gerador Série
frame5.pack(fill='both', expand=True)

# adicionando abas ao notebook
notebook.add(frame1, text='Menu')
notebook.add(frame2, text='Reatância Série')
notebook.add(frame3, text='Trasformador 1/4')
notebook.add(frame4, text='Stub Simples')
notebook.add(frame5, text='Stub Duplo')

# Menu

## Foto do menu 
img_menu = ImageTk.PhotoImage(Image.open("Images/menu.png"))
texto_menu = tk.Label(frame1, image=img_menu)
texto_menu.grid(row = 0, column = 0, columnspan=3,pady=20, padx=20, sticky="WE")

## Frame para armazenar as variáveis
variaveis = tk.LabelFrame(frame1, text= "Inputs ", padx=50, pady=10)
variaveis.grid(row = 1, column=0, padx=20)

## Variáveis
label_Zc = tk.Label(variaveis,text='Zc:').grid(row=0, column=0)
caixa_Zc = tk.Entry(variaveis, width=7)
caixa_Zc.insert(0, 50)
caixa_Zc.grid(row=0, column=1)

label_Zl = tk.Label(variaveis,text='Zl:').grid(row=1, column=0)
caixa_Zl = tk.Entry(variaveis, width=7)
caixa_Zl.insert(0, 20)
caixa_Zl.grid(row=1, column=1)

label_d = tk.Label(variaveis,text='d:').grid(row=2, column=0)
caixa_d = tk.Entry(variaveis, width=7)
caixa_d.insert(0, 24)
caixa_d.grid(row=2, column=1)

label_b = tk.Label(variaveis,text='Beta:').grid(row=3, column=0)
caixa_b = tk.Entry(variaveis, width=7)
caixa_b.insert(0, 24)
caixa_b.grid(row=3, column=1)

label_lbd = tk.Label(variaveis,text='Comprimento de onda:').grid(row=4, column=0)
caixa_lbd = tk.Entry(variaveis, width=7)
caixa_lbd.insert(0, 24)
caixa_lbd.grid(row=4, column=1)

label_f = tk.Label(variaveis,text='Frequância(Hz):').grid(row=0, column=2)
caixa_f = tk.Entry(variaveis, width=7)
caixa_f.insert(0, 0.01)
caixa_f.grid(row=0, column=3)

# Armazenando os inputs
def armazenar():
    Zc=float(caixa_Zc.get())
    Zl=float(caixa_Zl.get())
    d=float(caixa_d.get())
    b=float(caixa_b.get())
    lbd=float(caixa_lbd.get())
    f=float(caixa_f.get())




## Frame para armazenar alguns botões
botoes_menu = tk.LabelFrame(frame1, padx=50, pady=10, border=0)
botoes_menu.grid(row = 1, column=2, sticky="E")

### Botões do frame
botao_reat_ser = tk.Button(botoes_menu, text='Reatância Série', command=lambda:mudar_tab(notebook, frame2))
botao_reat_ser.grid(row=0, pady=3, sticky="WE")
botao_transf = tk.Button(botoes_menu, text='Tranformador 1/4', command=lambda:mudar_tab(notebook, frame3))
botao_transf.grid(row=1, pady=3, sticky="WE")
botao_stubsimples = tk.Button(botoes_menu, text='Stub Simples', command=lambda:mudar_tab(notebook, frame4))
botao_stubsimples.grid(row=2, pady=3, sticky="WE")
botao_stubduplo = tk.Button(botoes_menu, text='Stub Duplo', command=lambda:mudar_tab(notebook, frame4))
botao_stubduplo.grid(row=3, pady=3, sticky="WE")

#Cálculos e outputs do caso Reatância série
def simular_serie():
    f=float(caixa_f.get())
    t = np.arange(0, 1000, 0.1)
    y = np.cos(2*np.pi*f*t)

    # Colocando o grafico
    frame_grafico = tk.LabelFrame(frame2, padx=50, pady=50, border=0)
    frame_grafico.grid(row=1,column=1, padx=10)
    
    fig = Figure(figsize = (3.3, 3.3), dpi = 100)

    plt.plot(t, y)
    plt.title('Tensão na linha')
    plt.xlabel('t')
    plt.ylabel('V')
    plt.grid(True)
    plt.show()

    # Canvas do Tkinter que contém a figura
    canvas = FigureCanvasTkAgg(fig, master = frame_grafico)
    canvas.draw()

    # Colocando o Canvas na janela
    canvas.get_tk_widget().pack()
  
    # Menu abaixo do gráfico
    toolbar = NavigationToolbar2Tk(canvas,frame_grafico)
    toolbar.update()




# Aba casamento série(demais abas seguirão o mesmo padrão)
button_simularserie = tk.Button(frame2, width=16, height=3, text='Simular', command = lambda:simular_serie())
button_simularserie.grid(row=0, column=1, padx=200)

botao_menu_3 = tk.Button(frame2, width=16, height=3, text = "Menu", command = lambda:mudar_tab(notebook, frame1))
botao_menu_3.grid(row=0, column=2)



root.mainloop()
