# funções usadas no monthplan serão declaradas aqui

import tkinter as tk

def win_values(window, size, title):
    
    window.geometry(size)
    window.title(title)

def label(window, text, font_size):
    label = tk.Label(window, text=text, font = ('Arial', font_size))
    label.pack(padx = 20, pady = 20)


# Label Simples

