import tkinter as tk
from tkinter import RIGHT, Button, ttk
import numpy as np
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

# root window
root = tk.Tk()

# Adquirir tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width=screen_width-650
heigth=screen_height-250
root.geometry(f"{width}x{heigth}")

# root.geometry('800x600')
root.configure(bg="white")
root.title('Casa Impedância')


# Criando um notebook (Widget para manusear diferentes abas)
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

# add frames to notebook
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
caixa_Zc.insert(0, 0.19)
caixa_Zc.grid(row=0, column=1)

label_Zl = tk.Label(variaveis,text='Zl:').grid(row=1, column=0)
caixa_Zl = tk.Entry(variaveis, width=7)
caixa_Zl.insert(0, 10)
caixa_Zl.grid(row=1, column=1)

label_d = tk.Label(variaveis,text='d:').grid(row=2, column=0)
caixa_d = tk.Entry(variaveis, width=7)
caixa_d.insert(0, 24)
caixa_d.grid(row=2, column=1)

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




root.mainloop()