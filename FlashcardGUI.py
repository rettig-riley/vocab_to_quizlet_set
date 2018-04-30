"""FlashcardGUI.py
Purpose: Create a simple GUI for the quizlet.py file

Authors: Riley Rettig
Date created: January 17, 2018
Date last edited: April 30 2017
"""

from tkinter import *
from tkinter import messagebox

from quizlet import *


class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Create Set", fg="blue",
                             command=self.create_set)
        self.button.pack(side=BOTTOM)

        self.auth = Button(frame, text="Get Authorization", fg="blue",
                           command=self.auth_button)
        self.auth.pack(side=TOP)

        self.name_label = Label(text="Title")
        self.name = Text(height=1,width=20, borderwidth=1, relief=GROOVE)
        self.name_label.pack(side=TOP)
        self.name.pack(side=TOP)

        self.term_label = Label(text="Terms")
        self.terms = Text(height=20,width=30, borderwidth=1, relief=GROOVE)
        self.term_label.pack(side=LEFT)
        self.terms.pack(side=LEFT)

        self.def_label = Label(text="Definitions")
        self.definitions = Text(height=20, width=30, borderwidth=1,
                                relief=GROOVE)
        self.def_label.pack(side=LEFT)
        self.definitions.pack(side=LEFT)

        self.redirected_label = Label(text="Redirected URL")
        self.redirect_url = Text(height=1,width=15, borderwidth=1,
                                 relief=GROOVE)
        self.redirected_label.pack(side=BOTTOM)
        self.redirect_url.pack(side=BOTTOM)

        self.token_label = Label(text="Current Token")
        self.token = Label(text="", height = 1, width=15, borderwidth=1,
                           relief=GROOVE)
        self.token_label.pack(side=BOTTOM)
        self.token.pack(side=BOTTOM)

    def auth_button(self):
        ask_auth()
        self.token.config(text="")

    def create_set(self):
        if self.token["text"] == "":
            auth_code = get_auth(self.redirect_url.get(1.0, END))
            token = get_token(auth_code)
            self.token.config(text=token)
        else:
            token = self.token["text"]
        title = self.name.get(1.0, END)
        term_list = self.terms.get(1.0, END).split("\n")
        def_list = self.definitions.get(1.0, END).split("\n")
        temp = create_set(token, title, term_list, def_list)
        if temp:
            messagebox.showinfo('Result', 'Set Created Successfully!')
            self.name.delete(1.0, END)
            self.terms.delete(1.0, END)
            self.definitions.delete(1.0, END)

root = Tk()
app = App(root)
root.mainloop()
