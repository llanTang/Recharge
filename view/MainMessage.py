from tkinter import *


class MainMessage(object):
    def __init__(self, master=None):
        self.root = master
        msg1 = Message(self.root, text="1. choose the algorithm you want \n"
                                       "2. fill neccessary params", relief=FLAT, font=('楷体', 14),
                       width=500)
        msg1.place(relx=0.1, rely=0.1, relheight=0.4, relwidth=0.8)

