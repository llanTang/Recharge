from tkinter import *
from view.AlgorithmMessageView import AlgorithmMessageView


class BestPSOView(AlgorithmMessageView):
    def __init__(self, master=None):
        super(BestPSOView, self).__init__(master)
        # 其他条件
        algorithm_button = Button(self.frame_top, text="PSO", command=self.__run_algorithm__)
        algorithm_button.place(relx=0.4, rely=0.8, width=100)

    def __run_algorithm__(self):
        self.__run__("BestPSO")

