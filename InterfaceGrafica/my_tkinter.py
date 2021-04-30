import tkinter
from tkinter import messagebox

def envio():
    # messagebox.showinfo("Titulo", "Mensagem de informação!")
    """if messagebox.askyesno("Questão", "Mensagem de questionamento!") is True:
        data = entrada.get()
        texto.insert(tkinter.END, data)"""
    # messagebox.showerror("Title", "Mensagem de Error!")
    # messagebox.showwarning("Title", "Mensagem de Aviso!")
    """if messagebox.askokcancel("Title", "Mensagem de questionamento!") is True:
        window.destroy()"""


window = tkinter.Tk()
window.title("Socket Python")
window.geometry("500x500")
window.wm_iconbitmap("./icons/plug.ico")
window.resizable(False, False)

label = tkinter.Label(window, text="Nome: ")
label.place(x=5, y=10)

button1 = tkinter.Button(window, text="Send", bg="black", fg="yellow", height=1, width=5, command=envio)
button1.place(x=360, y=8)

entrada = tkinter.Entry(window, width=50)
entrada.place(x=50, y=10)

list1 = tkinter.Listbox(window, width=35, selectmode=tkinter.MULTIPLE)
list1.insert(1, "Pedra")
list1.insert(2, "Papel")
list1.insert(3, "Tesoura")
list1.place(x=25, y=40)

texto = tkinter.Text(window, width=28)
texto.place(x=250, y=40)

window.mainloop()