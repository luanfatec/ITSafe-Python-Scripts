import os
from tkinter import *
from tkinter import messagebox


def execute_command():
    try:
        _textbox.delete("1.0", 'end')
        command = _input1.get()
        _textbox.insert(END, os.popen(command).read())

    except Exception as msg:
        _textbox.delete("1.0", 'end')
        messagebox.showinfo("", msg)


main = Tk()
main.title("Executar comandos")
main.resizable(False, False)
main.geometry("550x600")
main["background"] = "#000000"

_button1 = Button(main, width=10, text="Executar", foreground="#00E855", bg="black", relief=SUNKEN,
                  command=execute_command)
_button1.place(x=435, y=10)

_label1 = Label(main, text="Comando: ", bg="black", fg="#00E855")
_label1.place(x=30, y=12)

_input1 = Entry(main, width=53, foreground="#00E855", bg="black")
_input1.place(x=100, y=14)
_input1.focus()

_textbox = Text(main, width=63, height=33, bg="#000154", fg="#0BDBCD")
_textbox.place(x=20, y=49)

main.mainloop()
