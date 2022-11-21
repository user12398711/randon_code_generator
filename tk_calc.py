from tkinter import *


class Calculator:
    def __init__(self):
        self.expression = ""
        self.equation = StringVar()

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except Exception as e:
            self.equation.set(" Error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def set_up(self, gui):
        expression_field = Entry(gui, textvariable=self.equation)
        expression_field.grid(columnspan=4, ipadx=70)

        button1 = Button(
            gui, text=" 1 ", fg="black", bg="red", command=lambda: self.press(1), height=1, width=7
        )
        button1.grid(row=2, column=0)
        button2 = Button(
            gui, text=" 2 ", fg="black", bg="red", command=lambda: self.press(2), height=1, width=7
        )
        button2.grid(row=2, column=1)
        button3 = Button(
            gui, text=" 3 ", fg="black", bg="red", command=lambda: self.press(3), height=1, width=7
        )
        button3.grid(row=2, column=2)
        button4 = Button(
            gui, text=" 4 ", fg="black", bg="red", command=lambda: self.press(4), height=1, width=7
        )
        button4.grid(row=3, column=0)
        button5 = Button(
            gui, text=" 5 ", fg="black", bg="red", command=lambda: self.press(5), height=1, width=7
        )
        button5.grid(row=3, column=1)
        button6 = Button(
            gui, text=" 6 ", fg="black", bg="red", command=lambda: self.press(6), height=1, width=7
        )
        button6.grid(row=3, column=2)
        button7 = Button(
            gui, text=" 7 ", fg="black", bg="red", command=lambda: self.press(7), height=1, width=7
        )
        button7.grid(row=4, column=0)
        button8 = Button(
            gui, text=" 8 ", fg="black", bg="red", command=lambda: self.press(8), height=1, width=7
        )
        button8.grid(row=4, column=1)
        button9 = Button(
            gui, text=" 9 ", fg="black", bg="red", command=lambda: self.press(9), height=1, width=7
        )
        button9.grid(row=4, column=2)
        button0 = Button(
            gui, text=" 0 ", fg="black", bg="red", command=lambda: self.press(0), height=1, width=7
        )
        button0.grid(row=5, column=0)
        plus = Button(
            gui,
            text=" + ",
            fg="black",
            bg="red",
            command=lambda: self.press("+"),
            height=1,
            width=7,
        )
        plus.grid(row=2, column=3)
        minus = Button(
            gui,
            text=" - ",
            fg="black",
            bg="red",
            command=lambda: self.press("-"),
            height=1,
            width=7,
        )
        minus.grid(row=3, column=3)
        multiply = Button(
            gui,
            text=" * ",
            fg="black",
            bg="red",
            command=lambda: self.press("*"),
            height=1,
            width=7,
        )
        multiply.grid(row=4, column=3)
        divide = Button(
            gui,
            text=" / ",
            fg="black",
            bg="red",
            command=lambda: self.press("/"),
            height=1,
            width=7,
        )
        divide.grid(row=5, column=3)
        equal = Button(
            gui, text=" = ", fg="black", bg="red", command=self.equalpress, height=1, width=7
        )
        equal.grid(row=5, column=2)
        clear = Button(
            gui, text="Clear", fg="black", bg="red", command=self.clear, height=1, width=7
        )
        clear.grid(row=5, column=1)
        Decimal = Button(
            gui, text=".", fg="black", bg="red", command=lambda: self.press("."), height=1, width=7
        )
        Decimal.grid(row=6, column=0)


if __name__ == "__main__":
    main_gui = Tk()
    main_gui.configure(background="light green")
    main_gui.title("Simple Calculator")
    main_gui.geometry("270x150")
    calculator = Calculator()
    calculator.set_up(main_gui)
    main_gui.mainloop()
