# -----------------------------------------------------------------------------

from tkinter import *

# -----------------------------------------------------------------------------


class UserInterface(Tk):

    # -------------------------------------------------------------------------

    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.geometry("1020x620")
        self.title("Etymological Relations")
        self.config(padx=20, pady=20)
        self.create_widgets()
        self.accommodate_widgets()

    # -------------------------------------------------------------------------

    def create_widgets(self):
        self.create_textvariables()
        self.label = Label(textvariable=self.label_text)
        self.entry = Entry(textvariable=self.entry_text)
        self.button = Button(textvariable=self.button_text,
                             command=self.button_func)

    # -------------------------------------------------------------------------

    def create_textvariables(self):
        self.label_text = StringVar()
        self.entry_text = StringVar()
        self.button_text = StringVar()
        self.button_text.set("Soy un boton")
        self.entry_text.set("Ingrese texto aquí")

    # -------------------------------------------------------------------------

    def accommodate_widgets(self):
        self.button.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.label.grid(row=0, column=2)

    # -------------------------------------------------------------------------

    def button_func(self):
        self.label_text.set(self.entry_text.get())
        print(self.entry_text.get())

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    UserInterface().mainloop()

# -----------------------------------------------------------------------------
