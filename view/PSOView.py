from tkinter import *
from view.AlgorithmMessageView import AlgorithmMessageView
from exception.ControllerException import ControllerException
import tkinter.messagebox



class PSOView(AlgorithmMessageView):
    def __init__(self, master=None):
        super(PSOView, self).__init__(master)
        # 其他条件
        algorithm_button = Button(self.frame_top, text="BestPSO", command=self.__run_algorithm__)
        algorithm_button.place(relx=0.4, rely=0.8, width=100)

    def __run_algorithm__(self):
        try:
            self.__run__("PSO")
        except ControllerException as e:
            tkinter.messagebox.showwarning("showwarning", "Error Message:\n%s" % e)


