from tkinter import *
from tkinter import ttk
from view.MainMessage import MainMessage
from view.PSOView import PSOView
from view.BestPSOView import BestPSOView
from utils.viewUtils import ViewUtils


class MainGUI(object):
    def __init__(self):
        self.root = Tk(className="充电站")
        self.root.geometry('800x800')
        self.frame_root = Frame(self.root)
        self.frame_root.pack()
        self.frame_left = Frame(self.frame_root, width=100, height=800)
        self.frame_right = Frame(self.frame_root, width=700, height=800)
        self.frame_left.pack(side='left')
        self.frame_right.pack(side='right')
        MainMessage(self.frame_right)
        self.__treeNavgation__(self.frame_left)
        self.root.mainloop()

    def __treeNavgation__(self, master):
        tree = ttk.Treeview(master, columns=['0', ], height=40, show='headings')
        tree.column('0', width=10, anchor='nw')
        tree.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)
        tree.heading('0', text='algorithm')
        tree.insert('', 3, values='PSO')
        tree.insert('', 1, values='BestPSO')
        tree.bind('<ButtonRelease-1>', self.__treeViewClick__)

    def __treeViewClick__(self, event):
        widget = event.widget
        try:
            selection = widget.selection()
            value = widget.item(selection[0], "values")
            print(value[0])
            switch = {'PSO': self.__psoMessageView__,
                      'BestPSO': self.__bestPSOMessageView__}
            switch.get(value[0])()
        except:
            return

    def __psoMessageView__(self):
        ViewUtils.destroyframe(self.frame_right)
        self.frame_right.message = PSOView(self.frame_right)

    def __bestPSOMessageView__(self):
        ViewUtils.destroyframe(self.frame_right)
        self.frame_right.message = BestPSOView(self.frame_right)

