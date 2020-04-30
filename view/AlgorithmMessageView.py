from tkinter import filedialog
from tkinter import *
import os
from controller import *
from utils.viewUtils import ViewUtils
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial
import numpy as np
from exception.ControllerException import ControllerException
from exception.CustomErrorCode import CustomErrorCode


class AlgorithmMessageView(object):
    '''
        弹出打开文件对话框
    '''

    def __init__(self, master=None):
        self.root = master
        self.frame_root = Frame(self.root)
        self.frame_root.pack()
        self.frame_bottom = Frame(self.frame_root, width=700, height=400)
        self.frame_bottom.pack(side='bottom')
        self.frame_top = Frame(self.frame_root, width=700, height=400)
        self.frame_top.pack(side='top')
        self.result_file = {}

        msg1 = Message(self.frame_top, text="PSO algorithm", relief=FLAT, font=('楷体', 14), width=500)
        msg1.place(relx=0.4, rely=0)

        # 迭代次数
        count_label = Label(self.frame_top, text="迭代次数:")
        count_label.place(relx=0.05, rely=0.1)
        self.count = IntVar()
        count_entry = Entry(self.frame_top, textvariable=self.count)
        count_entry.place(relx=0.15, rely=0.1, width=100)

        # 最大迭代次数
        count_max_label = Label(self.frame_top, text="最大迭代次数:")
        count_max_label.place(relx=0.35, rely=0.1)
        self.count_max = IntVar()
        count_max_entry = Entry(self.frame_top, textvariable=self.count_max)
        count_max_entry.place(relx=0.45, rely=0.1, width=100)

        # 种群数量
        size_label = Label(self.frame_top, text="种群数目:")
        size_label.place(relx=0.65, rely=0.1)
        self.size_value = IntVar(0)
        size_entry = Entry(self.frame_top, textvariable=self.size_value)
        size_entry.place(relx=0.75, rely=0.1, width=100)

        # 初投资成本
        cost_label = Label(self.frame_top, text="投资成本:")
        cost_label.place(relx=0.05, rely=0.2)
        self.cost_value = DoubleVar(0)
        cost_entry = Entry(self.frame_top, textvariable=self.cost_value)
        cost_entry.place(relx=0.15, rely=0.2, width=100)
        # 汽车充电功率
        power_label = Label(self.frame_top, text="充电功率:")
        power_label.place(relx=0.35, rely=0.2)
        self.power_value = DoubleVar(0)
        power_entry = Entry(self.frame_top, textvariable=self.power_value)
        power_entry.place(relx=0.45, rely=0.2, width=100)

        # 负载率
        load_label = Label(self.frame_top, text="负载率:")
        load_label.place(relx=0.65, rely=0.2)
        self.load_value = DoubleVar(0)
        load_entry = Entry(self.frame_top, textvariable=self.load_value)
        load_entry.place(relx=0.75, rely=0.2, width=100)

        # 单位距离损耗
        loss_label = Label(self.frame_top, text="单位距离损耗:")
        loss_label.place(relx=0.05, rely=0.3)
        self.loss_value = DoubleVar(0)
        loss_entry = Entry(self.frame_top, textvariable=self.loss_value)
        loss_entry.place(relx=0.15, rely=0.3, width=100)

        # 回收年限
        payback_label = Label(self.frame_top, text="回收年限:")
        payback_label.place(relx=0.35, rely=0.3)
        self.payback_value = DoubleVar(0)
        payback_entry = Entry(self.frame_top, textvariable=self.payback_value)
        payback_entry.place(relx=0.45, rely=0.3, width=100)

        # 充电效率
        ratio_label = Label(self.frame_top, text="充电效率:")
        ratio_label.place(relx=0.65, rely=0.3)
        self.ratio_value = DoubleVar(0)
        ratio_entry = Entry(self.frame_top, textvariable=self.ratio_value)
        ratio_entry.place(relx=0.75, rely=0.3, width=100)

        # 贴现率
        covert_factor_label = Label(self.frame_top, text="贴现率:")
        covert_factor_label.place(relx=0.05, rely=0.4)
        self.covert_factor_value = DoubleVar(0)
        covert_factor_entry = Entry(self.frame_top, textvariable=self.covert_factor_value)
        covert_factor_entry.place(relx=0.15, rely=0.4, width=100)
        # 充电站配电量
        charge_count_label = Label(self.frame_top, text="配电量:")
        charge_count_label.place(relx=0.35, rely=0.4)
        self.charge_count_value = DoubleVar(0)
        charge_count_entry = Entry(self.frame_top, textvariable=self.charge_count_value)
        charge_count_entry.place(relx=0.45, rely=0.4, width=100)
        # 折算系数
        discount_ratio_label = Label(self.frame_top, text="折算系数:")
        discount_ratio_label.place(relx=0.65, rely=0.4)
        self.discount_ratio_value = DoubleVar(0)
        discount_ratio_entry = Entry(self.frame_top, textvariable=self.discount_ratio_value)
        discount_ratio_entry.place(relx=0.75, rely=0.4, width=100)

        # 道路曲折系数
        tortuo_label = Label(self.frame_top, text="道路曲折系数:")
        tortuo_label.place(relx=0.05, rely=0.5)
        self.tortuo_value = DoubleVar(0)
        tortuo_entry = Entry(self.frame_top, textvariable=self.tortuo_value)
        tortuo_entry.place(relx=0.15, rely=0.5, width=100)
        # 每天充电次数
        charge_per_day_label = Label(self.frame_top, text="每天充电次数:")
        charge_per_day_label.place(relx=0.35, rely=0.5)
        self.charge_per_day_value = IntVar(0)
        charge_per_day_entry = Entry(self.frame_top, textvariable=self.charge_per_day_value)
        charge_per_day_entry.place(relx=0.45, rely=0.5, width=100)
        # 服务半径
        radius_label = Label(self.frame_top, text="服务半径:")
        radius_label.place(relx=0.65, rely=0.5)
        self.radius_value = DoubleVar(0)
        radius_entry = Entry(self.frame_top, textvariable=self.radius_value)
        radius_entry.place(relx=0.75, rely=0.5, width=100)

        # 加速因子
        acc_ratio_label = Label(self.frame_top, text="加速因子:")
        acc_ratio_label.place(relx=0.05, rely=0.6)
        self.acc_ratio_value = DoubleVar(0)
        acc_ratio_entry = Entry(self.frame_top, textvariable=self.acc_ratio_value)
        acc_ratio_entry.place(relx=0.15, rely=0.6, width=100)

        # 小区数据
        area_label = Label(self.frame_top, text="小区数据:")
        area_label.place(relx=0.35, rely=0.6)
        area_button = Button(self.frame_top, text="选择文件", command=partial(self.__loadFileDialog__, "area_file"))
        area_button.place(relx=0.45, rely=0.6, width=100)

        # 预选充电站
        station_label = Label(self.frame_top, text="预选充电站:")
        station_label.place(relx=0.65, rely=0.6)
        station_button = Button(self.frame_top, text="选择文件",
                                command=partial(self.__loadFileDialog__, "station_file"))
        station_button.place(relx=0.75, rely=0.6, width=100)

    def __loadFileDialog__(self, filePath):
        # 设置选择的文件类型
        my_fileTypes = [('text files', '.txt')]

        # 请求选择文件
        self.result_file[filePath] = filedialog.askopenfilename(parent=self.root,
                                                                initialdir=os.getcwd(),
                                                                title='please select a file:',
                                                                filetypes=my_fileTypes)

    def __run__(self, algorithm):
        psoController = PSOController()
        self.station_file = self.result_file['station_file']
        self.area_file = self.result_file['area_file']
        print(self.station_file)
        data, data_count = fileController.readFile(self.area_file)
        station, station_count = fileController.readFile(self.station_file)
        count_max = self.count_max.get()
        cost = self.cost_value.get()
        power = self.power_value.get()
        load = self.load_value.get()
        loss = self.loss_value.get()
        payback = self.payback_value.get()
        ratio = self.ratio_value.get()
        covert_factor = self.covert_factor_value.get()
        charge_count = self.charge_count_value.get()
        discount_ratio = self.discount_ratio_value.get()
        tortuo = self.tortuo_value.get()
        charge_per_day = self.charge_per_day_value.get()
        radius = self.radius_value.get()
        acc_ratio = self.acc_ratio_value.get()
        car_count = sum([x[2] for x in data])
        size = self.size_value.get()

        self.bestStationCount = psoController.calculateBestStationCount(charge_per_day, car_count, power, load,
                                                                        charge_count, ratio)
        if self.bestStationCount > station_count:
            print("best car count" +str(self.bestStationCount))
            raise ControllerException(CustomErrorCode.PARAM_ERROR, "参数错误")
        self.fit_var_list, self.best_pos, self.g = psoController.run(data, data_count, station, station_count, 5, size,
                                                                     count_max,
                                                                     1, radius, algorithm, acc_ratio, acc_ratio)
        self.cost = psoController.calculateCost(cost, covert_factor, payback, 5, discount_ratio, charge_per_day, tortuo,
                                                loss, self.fit_var_list[-1])

        # 最佳充电站位置
        ViewUtils.destroyframe(self.frame_bottom)

        self.frame_label = Frame(self.frame_bottom, width=700, height=100)
        self.frame_label.pack(side='top')
        self.frame_plot = Frame(self.frame_bottom, width=700, height=300)
        self.frame_plot.pack(side='bottom')
        size_label = Label(self.frame_label, text="最佳充电站:" + str(self.best_pos))
        size_label.place(relx=0, rely=0)
        cost_label = Label(self.frame_label, text="预估成本:" + str(self.cost))
        cost_label.place(relx=0.5, rely=0)

        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)

        a.plot(np.linspace(0, count_max, count_max), self.fit_var_list, c="R", alpha=0.5)
        canvas = FigureCanvasTkAgg(f, master=self.frame_plot)
        canvas.draw()  # 注意show方法已经过时了,这里改用draw
        canvas.get_tk_widget().pack(side=TOP,  # 上对齐
                                    fill=BOTH,  # 填充方式
                                    expand=YES)  # 随窗口大小调整而调整
