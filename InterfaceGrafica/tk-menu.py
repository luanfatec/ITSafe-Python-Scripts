import tkinter
from tkinter import messagebox


def sair():
    if messagebox.askokcancel("", "Deseja realmente sair?") is True:
        window.destroy()


def nova_janela():
    topp = tkinter.Toplevel()
    topp.title("Socket Client")
    topp.geometry("100x100")
    topp.resizable(False, False)


window = tkinter.Tk()
window.title("Socket Python")
window.geometry("500x500")
window.resizable(False, False)

menu = tkinter.Menu(window)
novo_item = tkinter.Menu(menu)
novo_item.add_command(label="Novo", command=nova_janela)
novo_item.add_command(label="Editar")
novo_item.add_separator()
novo_item.add_command(label="Sair", command=sair)

menu.add_cascade(label="Arquivo", menu=novo_item)
window.config(menu=menu)
window.mainloop()
