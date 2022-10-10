
import tkinter
from tkinter import ttk


window = tkinter.Tk()

lista = ['piton', 'gato', 'puma', 'leon', 'tortuga']
listaItem = tkinter.StringVar(value=lista)
listBox = tkinter.ListBox(window, height=100, listvariable=listaItem)
listBox.grid(column=0, row=0, sticky=tkinter.W)



window.columnconfigure(0, weight=3)
window.columnconfigure(0, weight=3)

label= ttk.Label(window, text='Soy la etiqueta')
label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)



window.mainloop()



