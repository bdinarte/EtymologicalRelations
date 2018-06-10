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

        self.lf_word_x_word = LabelFrame(text="Operaciones entre palabras")
        self.lf_word_x_lang = LabelFrame(text="Operaciones palabra e idioma")
        self.lf_lang_x_lang = LabelFrame(text="Operaciones idioma e idioma")
        self.lf_relations = LabelFrame(text="Opciones generales")

        self.lf_word_x_word.grid(row=0, column=0)
        self.lf_word_x_lang.grid(row=0, column=1)
        self.lf_lang_x_lang.grid(row=1, column=0)
        self.lf_relations.grid(row=1, column=1)

    # -------------------------------------------------------------------------

    def create_widgets(self):
        self.create_widgets_word_x_word()
        self.create_widgets_word_x_lang()
        self.create_widgets_lang_x_lang()

    # -------------------------------------------------------------------------

    def create_widgets_word_x_word(self):

        self.word_x = StringVar()
        self.word_y = StringVar()
        self.result_word_x_word = StringVar()

        self.label_word_x = Label(self.lf_word_x_word, text="Palabra X")
        self.label_word_y = Label(self.lf_word_x_word, text="Palabra Y")
        self.label_result_word_x_word = Label(self.lf_word_x_word, text="Resultado")

        self.entry_word_x = Entry(self.lf_word_x_word, textvariable=self.word_x)
        self.entry_word_y = Entry(self.lf_word_x_word, textvariable=self.word_y)
        self.entry_result_word_x_word = Entry(self.lf_word_x_word, textvariable=self.result_word_x_word)

        self.btn_is_son = Button(self.lf_word_x_word, text="Es hija X de Y", command=self.is_son)
        self.btn_is_uncle = Button(self.lf_word_x_word, text="Es tía X de Y", command=self.is_uncle)
        self.btn_are_cousins = Button(self.lf_word_x_word, text="Son primas", command=self.are_cousins)
        self.btn_are_siblings = Button(self.lf_word_x_word, text="Son hermanas", command=self.are_siblings)
        self.btn_cousin_grade = Button(self.lf_word_x_word, text="Grado primas", command=self.cousin_grade)

    # -------------------------------------------------------------------------

    def create_widgets_word_x_lang(self):

        self.word_p = StringVar()
        self.word_d = StringVar()
        self.result_word_x_lang = StringVar()

        self.label_word_p = Label(self.lf_word_x_lang, text="Palabra P")
        self.label_word_d = Label(self.lf_word_x_lang, text="Palabra D")
        self.label_result_word_x_lang = Label(self.lf_word_x_lang, text="Resultado")

        self.entry_word_p = Entry(self.lf_word_x_lang, textvariable=self.word_p)
        self.entry_word_d = Entry(self.lf_word_x_lang, textvariable=self.word_d)
        self.entry_result_word_x_lang = Entry(self.lf_word_x_lang, textvariable=self.result_word_x_lang)

        self.btn_p_is_related_d = Button(self.lf_word_x_lang, text="P se relaciona con D", command=self.p_is_related_d)
        self.btn_p_yields_d = Button(self.lf_word_x_lang, text="Palabras originadas por P en D", command=self.p_yields_d)
        self.btn_langs_related_p = Button(self.lf_word_x_lang, text="Idiomas relacionados con P", command=self.langs_related_p)
        self.list_word_x_lang = Listbox(self.lf_word_x_lang)

    # -------------------------------------------------------------------------

    def create_widgets_lang_x_lang(self):

        self.lang_x = StringVar()
        self.lang_y = StringVar()
        self.result_lang_x_lang = StringVar()

        self.label_lang_x = Label(self.lf_lang_x_lang, text="Palabra P")
        self.label_lang_y = Label(self.lf_lang_x_lang, text="Palabra D")
        self.label_result_lang_x_lang = Label(self.lf_lang_x_lang, text="Resultado")

        self.entry_lang_x = Entry(self.lf_lang_x_lang, textvariable=self.lang_x)
        self.entry_lang_y = Entry(self.lf_lang_x_lang, textvariable=self.lang_y)
        self.entry_result_lang_x_lang = Entry(self.lf_lang_x_lang, textvariable=self.result_lang_x_lang)

        self.btn_amount_of_common_words = Button(self.lf_lang_x_lang, text="Cantidad palabras comunes", command=self.amount_of_common_words)
        self.btn_common_words = Button(self.lf_lang_x_lang, text="Listar palabras comunes", command=self.common_words)
        self.btn_greater_contribution = Button(self.lf_lang_x_lang, text="Idioma que más aporto a X", command=self.greater_contribution)
        self.btn_contribution_by_lang = Button(self.lf_lang_x_lang, text="Porcentajes de aporte a X", command=self.contribution_by_lang)
        self.list_lang_x_lang = Listbox(self.lf_lang_x_lang)

    # -------------------------------------------------------------------------

    def accommodate_widgets(self):

        # ---------------------------------------------------------------------
        # Operaciones palabra entre palabra
        # ---------------------------------------------------------------------

        self.label_word_x.grid(row=0, column=0, sticky=NW, padx=5)
        self.label_word_y.grid(row=0, column=1, sticky=NW, padx=5)
        self.label_result_word_x_word.grid(row=0, column=2, sticky=NW, padx=5)

        self.entry_word_x.grid(row=1, column=0)
        self.entry_word_y.grid(row=1, column=1)
        self.entry_result_word_x_word.grid(row=1, column=2)

        self.btn_cousin_grade.grid(row=1, column=3)
        self.btn_is_son.grid(row=2, column=0)
        self.btn_is_uncle.grid(row=2, column=1)
        self.btn_are_siblings.grid(row=2, column=2)
        self.btn_are_cousins.grid(row=2, column=3)

        # ---------------------------------------------------------------------
        # Operaciones palabra e idioma
        # ---------------------------------------------------------------------

        self.label_word_d.grid(row=0, column=0, sticky=NW, padx=5)
        self.label_word_p.grid(row=0, column=1, sticky=NW, padx=5)
        self.label_result_word_x_lang.grid(row=0, column=2, sticky=NW, padx=5)

        self.entry_word_d.grid(row=1, column=0)
        self.entry_word_p.grid(row=1, column=1)
        self.entry_result_word_x_lang.grid(row=1, column=2)

        self.btn_p_is_related_d.grid(row=1, column=3, columnspan=2)
        self.btn_p_yields_d.grid(row=2, column=3, columnspan=2)
        self.btn_langs_related_p.grid(row=3, column=3, columnspan=2)

        self.list_word_x_lang.grid(row=2, column=0, columnspan=1, rowspan=8)

        # ---------------------------------------------------------------------
        # Operaciones idioma entre idioma
        # ---------------------------------------------------------------------

        self.label_lang_x.grid(row=0, column=0, sticky=NW, padx=5)
        self.label_lang_y.grid(row=0, column=1, sticky=NW, padx=5)
        self.label_result_lang_x_lang.grid(row=0, column=2, sticky=NW, padx=5)

        self.entry_lang_x.grid(row=1, column=0)
        self.entry_lang_y.grid(row=1, column=1)
        self.entry_result_lang_x_lang.grid(row=1, column=2)

        self.btn_amount_of_common_words.grid(row=1, column=3, columnspan=2)
        self.btn_common_words.grid(row=2, column=3, columnspan=2)
        self.btn_greater_contribution.grid(row=3, column=3, columnspan=2)
        self.btn_contribution_by_lang.grid(row=4, column=3, columnspan=2)

        self.list_lang_x_lang.grid(row=2, column=0, columnspan=1, rowspan=8)

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

    # -------------------------------------------------------------------------

    def p_is_related_d(self):
        self.result_word_x_lang.set("P está relacionada con D")

    # -------------------------------------------------------------------------

    def p_yields_d(self):
        self.result_word_x_lang.set("Palabras producidas")

    # -------------------------------------------------------------------------

    def langs_related_p(self):
        self.result_word_x_lang.set("Lenguajes relacionados con P")

    # -------------------------------------------------------------------------

    def amount_of_common_words(self):
        self.result_lang_x_lang.set("12")

    # -------------------------------------------------------------------------

    def common_words(self):
        self.result_lang_x_lang.set("Palabras comunes")

    # -------------------------------------------------------------------------

    def greater_contribution(self):
        self.result_lang_x_lang.set("Latín")

    # -------------------------------------------------------------------------

    def contribution_by_lang(self):
        self.result_lang_x_lang.set("Porcentaje de contribuciones al lenguaje")

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    UserInterface().mainloop()

# -----------------------------------------------------------------------------
