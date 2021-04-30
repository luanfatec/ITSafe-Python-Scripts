from tkinter import *


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def divisao(num1, num2):
    return num1 / num2


def multiplicacao(num1, num2):
    return num1 * num2


def operations(num1, action, num2):
   if action == "+":
      display.delete(0, 'end')
      display.insert(END, soma(int(num1), int(num2)))

   elif action == "-":
      display.delete(0, 'end')
      display.insert(END, subtracao(int(num1), int(num2)))

   elif action == "*":
      display.delete(0, 'end')
      display.insert(END, multiplicacao(int(num1), int(num2)))

   elif action == "/":
      display.delete(0, 'end')
      display.insert(END, divisao(int(num1), int(num2)))

   else:
      display.delete(0, "end")
      display.insert(END, "Error!")


def get_values0():
    display.insert(END, _button1.getvar("var0"))


def get_values1():
    display.insert(END, _button1.getvar("var1"))


def get_values2():
    display.insert(END, _button1.getvar("var2"))


def get_values3():
    display.insert(END, _button1.getvar("var3"))


def get_values4():
    display.insert(END, _button1.getvar("var4"))


def get_values5():
    display.insert(END, _button1.getvar("var5"))


def get_values6():
    display.insert(END, _button1.getvar("var6"))


def get_values7():
    display.insert(END, _button1.getvar("var7"))


def get_values8():
    display.insert(END, _button1.getvar("var8"))


def get_values9():
    display.insert(END, _button1.getvar("var9"))


def get_adcao():
    display.insert(END, _button1.getvar("adcao"))


def get_subtracao():
    display.insert(END, _button1.getvar("subtracao"))


def get_multi():
    display.insert(END, _button1.getvar("multi"))


def get_division():
    display.insert(END, _button1.getvar("division"))


def get_clear():
    display.delete(0, "end")


def get_equal():
   try:
     operation = display.get().split()
     operations(operation[0], operation[1], operation[2])

   except Exception as msg:
      print(msg)
      display.delete(0, "end")
      display.insert(END, "Operação não permitida!")


window = Tk()
window.title("Calculadora")
window.resizable(False, False)
window.geometry("425x240")
window["background"] = "#2A4359"

display = Entry(window, width=67)
display.place(x=10, y=17)
display["background"] = "#B6D0F2"

# Start - line 01
_button1 = Button(window, width=12, height=2, text=1, command=get_values1)
_button1.setvar(name="var1", value=1)
_button1.place(x=10, y=50)

_button2 = Button(window, width=12, height=2, text=2, command=get_values2)
_button2.setvar(name="var2", value=2)
_button2.place(x=110, y=50)

_button3 = Button(window, width=12, height=2, text=3, command=get_values3)
_button3.setvar(name="var3", value=3)
_button3.place(x=210, y=50)

_button4 = Button(window, width=12, height=2, text="+", command=get_adcao)
_button4.setvar(name="adcao", value=" + ")
_button4.place(x=320, y=50)
# End - line 01

# Start - line 02
_button5 = Button(window, width=12, height=2, text=4, command=get_values4)
_button5.setvar(name="var4", value=4)
_button5.place(x=10, y=95)

_button6 = Button(window, width=12, height=2, text=5, command=get_values5)
_button6.setvar(name="var5", value=5)
_button6.place(x=110, y=95)

_button7 = Button(window, width=12, height=2, text=6, command=get_values6)
_button7.setvar(name="var6", value=6)
_button7.place(x=210, y=95)

_button8 = Button(window, width=12, height=2, text="-", command=get_subtracao)
_button8.setvar(name="subtracao", value=" - ")
_button8.place(x=320, y=95)
# End - line 02

# Start - line 03
_button9 = Button(window, width=12, height=2, text=7, command=get_values7)
_button9.setvar(name="var7", value=7)
_button9.place(x=10, y=140)

_button10 = Button(window, width=12, height=2, text=8, command=get_values8)
_button10.setvar(name="var8", value=8)
_button10.place(x=110, y=140)

_button11 = Button(window, width=12, height=2, text=9, command=get_values9)
_button11.setvar(name="var9", value=9)
_button11.place(x=210, y=140)

_button12 = Button(window, width=12, height=2, text="*", command=get_multi)
_button12.setvar(name="multi", value=" * ")
_button12.place(x=320, y=140)
# End - line 03

# Start - line 04
_button13 = Button(window, width=12, height=2, text="limpar", command=get_clear)
_button13.setvar(name="clear", value="limpar")
_button13.place(x=10, y=185)

_button14 = Button(window, width=12, height=2, text=0, command=get_values0)
_button14.setvar(name="var0", value=0)
_button14.place(x=110, y=185)

_button15 = Button(window, width=12, height=2, text="=", command=get_equal)
_button15.setvar(name="equal", value=" = ")
_button15.place(x=210, y=185)

_button15 = Button(window, width=12, height=2, text="/", command=get_division)
_button15.setvar(name="division", value=" / ")
_button15.place(x=320, y=185)
# End - line 04

window.mainloop()
