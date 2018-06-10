# -----------------------------------------------------------------------------

from tkinter import *

# -----------------------------------------------------------------------------


class UserInterface(Tk):

    # -------------------------------------------------------------------------

    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.geometry("1220x700")
        self.title("Etymological Relations")
        self.config(padx=20, pady=20)
        self.create_frames()
        self.create_widgets()
        self.accommodate_widgets()

    # -------------------------------------------------------------------------

    def create_frames(self):

        self.lf_word_x_word = LabelFrame(text="This is a LabelFrame")
        self.lf_word_x_lang = LabelFrame(text="This is a LabelFrame")
        self.lf_lang_x_lang = LabelFrame(text="This is a LabelFrame")
        self.lf_relations = LabelFrame(text="This is a LabelFrame")

        self.lf_word_x_word.grid(row=0, column=0)
        self.lf_lang_x_lang.grid(row=0, column=1)
        self.lf_lang_x_lang.grid(row=1, column=0)
        self.lf_relations.grid(row=1, column=1)

    # -------------------------------------------------------------------------

    def create_widgets(self):
        self.create_widgets_word_x_word()
        self.create_widgets_word_x_lang()

    # -------------------------------------------------------------------------

    def create_widgets_word_x_word(self):

        self.word_x = StringVar()
        self.word_y = StringVar()
        self.result_word_x_word = StringVar()

        self.label_word_x = Label(text="Palabra X")
        self.label_word_y = Label(text="Palabra Y")
        self.label_result_word_x_word = Label(text="Resultado")

        self.entry_word_x = Entry(textvariable=self.word_x)
        self.entry_word_y = Entry(textvariable=self.word_y)
        self.entry_result = Entry(textvariable=self.result_word_x_word)

        self.btn_is_son = Button(text="Es hija X de Y", command=self.is_son)
        self.btn_is_uncle = Button(text="Es tía X de Y", command=self.is_uncle)
        self.btn_are_cousins = Button(text="Son primas", command=self.are_cousins)
        self.btn_are_siblings = Button(text="Son hermanas", command=self.are_siblings)
        self.btn_cousin_grade = Button(text="Grado primas", command=self.cousin_grade)

    # -------------------------------------------------------------------------

    def create_widgets_word_x_lang(self):

        self.word_x = StringVar()
        self.word_y = StringVar()
        self.result_word_x_word = StringVar()

        self.label_word_x = Label(self.lf_word_x_word, text="Palabra X")
        self.label_word_y = Label(self.lf_word_x_word, text="Palabra Y")
        self.label_result_word_x_word = Label(self.lf_word_x_word, text="Resultado")

        self.entry_word_x = Entry(self.lf_word_x_word, textvariable=self.word_x)
        self.entry_word_y = Entry(self.lf_word_x_word, textvariable=self.word_y)
        self.entry_result = Entry(self.lf_word_x_word, textvariable=self.result_word_x_word)

        self.btn_is_son = Button(self.lf_word_x_word, text="Es hija X de Y", command=self.is_son)
        self.btn_is_uncle = Button(self.lf_word_x_word, text="Es tía X de Y", command=self.is_uncle)
        self.btn_are_cousins = Button(self.lf_word_x_word, text="Son primas", command=self.are_cousins)
        self.btn_are_siblings = Button(self.lf_word_x_word, text="Son hermanas", command=self.are_siblings)
        self.btn_cousin_grade = Button(self.lf_word_x_word, text="Grado primas", command=self.cousin_grade)

    # -------------------------------------------------------------------------

    def accommodate_widgets(self):

        self.label_word_x.grid(row=0, column=0, sticky=NW, padx=5)
        self.label_word_y.grid(row=0, column=1, sticky=NW, padx=5)
        self.label_result_word_x_word.grid(row=0, column=2, sticky=NW, padx=5)

        self.entry_result.grid(row=0, column=2)
        self.entry_word_x.grid(row=1, column=0)
        self.entry_word_x.config(width=25)
        self.entry_word_y.grid(row=1, column=1)
        self.entry_result.grid(row=1, column=2)

        self.btn_cousin_grade.grid(row=1, column=3)
        self.btn_is_son.grid(row=2, column=0)
        self.btn_is_uncle.grid(row=2, column=1)
        self.btn_are_siblings.grid(row=2, column=2)
        self.btn_are_cousins.grid(row=2, column=3)

    # -------------------------------------------------------------------------

    def is_son(self):
        self.result_word_x_word.set("SÍ")

    # -------------------------------------------------------------------------

    def is_uncle(self):
        self.result_word_x_word.set("NO")
    # -------------------------------------------------------------------------

    def are_cousins(self):
        self.result_word_x_word.set("NO")

    # -------------------------------------------------------------------------

    def are_siblings(self):
        self.result_word_x_word.set("SÍ")

    # -------------------------------------------------------------------------

    def cousin_grade(self):
        self.result_word_x_word.set("2*")

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    UserInterface().mainloop()

# -----------------------------------------------------------------------------
