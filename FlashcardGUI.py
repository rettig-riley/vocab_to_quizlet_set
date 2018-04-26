# from tkinter import *
#
# root = Tk() #Create a Tk root widget (window with title bar and other decorations)
#             #Should only create one root widget for each program and must be created first
#
# w = Label(root, text="Hello, world!") #create label widget as a child to root window
# w.pack() #size itself to fir te text and become visible
#
# root.mainloop() #eventloop - appears and continues loop until window is closed
#####################
from tkinter import *
from tkinter import messagebox
from quizlet import *

class App:

    def __init__(self, master):

        frame = Frame(master) # frame is a simple container
        frame.pack() #makes frame visible

        self.button = Button(frame, text="Create Set", fg="blue", command=self.createSet)
        self.button.pack(side=BOTTOM)

        self.auth = Button(frame, text="Get Authorization", fg="blue", command=self.authButton)
        self.auth.pack(side=TOP)

        self.nameLabel = Label(text="Title")
        self.name = Text(height=1,width=20,borderwidth=1, relief = GROOVE)
        self.nameLabel.pack(side=TOP)
        self.name.pack(side=TOP)

        self.termLabel = Label(text="Terms")
        self.terms = Text(height=20,width=30,borderwidth=1, relief = GROOVE)
        self.termLabel.pack(side=LEFT)
        self.terms.pack(side=LEFT)

        self.defLabel = Label(text="Definitions")
        self.defs = Text(height=20,width=30, borderwidth=1, relief = GROOVE)
        self.defLabel.pack(side=LEFT)
        self.defs.pack(side=LEFT)

        self.redirectedLabel = Label(text="Redirected URL")
        self.redirectURL = Text(height=1,width=15, borderwidth=1, relief = GROOVE)
        self.redirectedLabel.pack(side=BOTTOM)
        self.redirectURL.pack(side=BOTTOM)

        self.tokenLabel = Label(text="Current Token")
        self.token = Label(text="", height = 1, width=15, borderwidth=1, relief = GROOVE)
        self.tokenLabel.pack(side=BOTTOM)
        self.token.pack(side=BOTTOM)

    def authButton(self):
        askAuth()
        self.token.config(text="")

    def createSet(self):
        if self.token["text"]=="":
            authCode = getAuth(self.redirectURL.get(1.0,END))
            token = requestToken(authCode)
            self.token.config(text=token)
        else:
            token = self.token["text"]
        title = self.name.get(1.0,END)
        termList = self.terms.get(1.0,END).split("\n")
        defList = self.defs.get(1.0,END).split("\n")
        temp = createSet(token, title, termList, defList)
        if temp:
            messagebox.showinfo('Result', 'Set Created Successfully!')
            self.name.delete(1.0, END)
            self.terms.delete(1.0,END)
            self.defs.delete(1.0,END)


root = Tk()

app = App(root)

root.mainloop()

#root.destroy() # optional