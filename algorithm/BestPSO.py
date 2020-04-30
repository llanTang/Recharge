import numpy as np
import random
from itertools import combinations
from .BaseAlg import Particle
from exception.ControllerException import ControllerException
from exception.CustomErrorCode import CustomErrorCode


def fit_fun(data, station, g):  # 适应函数
    value = 0.0
    for i in range(np.shape(data)[0]):
        dist = ((data[i][0] - station[g[i]][0]) ** 2 + (data[i][1] - station[g[i]][1]) ** 2) ** 0.5
        value = value + dist * data[i][2]
    return value

class BestPSO:
    def __init__(self, data, data_num, station, station_count, station_num, size, iter_num, max_vel,
                 radius,
                 C1, C2,
                 best_fitness_value=float('Inf'),
                  W=1):
        self.C1 = C1
        self.C2 = C2
        self.W = W
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.max_vel = max_vel  # 粒子最大速度
        self.station_count = station_count
        self.station_num = station_num
        self.data_num = data_num
        self.radius = radius
        self.data = data
        self.station = station
        self.best_fitness_value = best_fitness_value
        self.best_station = np.zeros(station_count)
        self.fitness_val_list = []  # 每次迭代最优适应值
        self.Particle_list = []
        self.station_all = self.calculate_station_all()
        if self.station_all is None:
            raise ControllerException(CustomErrorCode.PARAM_ERROR,"参数错误")
        for i in self.station_all[0]:
            self.best_station[i] = 1
        #self.g = self.calculate_g(self.station_all[0])
        for i in range(self.size):
            index = random.sample(range(np.shape(self.station_all)[0]), 1)[0]
            g = self.calculate_g(self.station_all[index])
            station_def = np.zeros(station_count)
            for station_index in self.station_all[index]:
                station_def[station_index] = 1
            fitnessValue = fit_fun(data, station, g)
            particle = Particle(data, station, station_def, g, fitnessValue)
            self.Particle_list.append(particle)

    def set_bestFitnessValue(self, value):
        self.best_fitness_value = value

    def get_bestFitnessValue(self):
        return self.best_fitness_value

    def set_bestStation(self, value):
        self.best_station = value

    def get_bestStation(self):
        return self.best_station

    def calculate_station_all(self):
        result = []
        for ll in list(combinations(range(self.station_count), self.station_num)):
            flag = 0
            for d in self.data:
                distance = []
                for l in ll:
                    dis = (d[0] - self.station[l][0]) ** 2 + (d[1] - self.station[l][1]) ** 2
                    # print(dis, l)
                    distance.append(dis)
                if min(distance) > self.radius ** 2:
                    flag = 1
            if flag == 0:
                result.append(ll)
        return result

    def calculate_g(self, station_choose):
        g = []
        for j in range(self.data_num):
            distance = []
            for station_index in station_choose:
                dis = (self.data[j][0] - self.station[station_index][0]) ** 2 + (
                        self.data[j][1] - self.station[station_index][1]) ** 2
                distance.append(dis)
            min_station_index = station_choose[distance.index(min(distance))]
            g.append(min_station_index)
        return g

    # 更新速度
    def update_vel(self, part):
        for i in range(self.station_count):
            vel_value = self.W * part.get_vel()[i] + self.C1 * random.random() * (
                    part.get_best_station_def()[i] - part.get_station_def()[i]) \
                        + self.C2 * random.random() * (self.get_bestStation()[i] - part.get_station_def()[i])
            if vel_value > self.max_vel:
                vel_value = self.max_vel
            elif vel_value < -self.max_vel:
                vel_value = -self.max_vel
            part.set_vel(i, vel_value)

    def update_pos_one(self, part):
        pos_list = []
        for i in range(self.station_count):
            pos_value = np.abs(part.get_station_def()[i] + part.get_vel()[i])
            pos_list.append((pos_value, i))
        list.sort(pos_list, key=lambda x: x[0], reverse=True)
        sort_index = []
        for ll in self.station_all:
            sort_value = 0
            for l in ll:
                for i in range(self.station_count):
                    if pos_list[i][1] == l:
                        sort_value = sort_value + i
                        break
            sort_index.append(sort_value)
        choose_station = self.station_all[sort_index.index(min(sort_index))]
        g = self.calculate_g(choose_station)
        station_def_test = np.zeros(self.station_count)
        for i in range(self.station_num):
            station_def_test[choose_station[i]] = 1
        part.set_station_def(station_def_test)
        part.set_g(g)
        value = fit_fun(part.get_data(), part.get_station(), part.get_g())
        if value < part.get_fitness_value():
            part.set_fitness_value(value)
            part.set_best_station_def(station_def_test)
        if value < self.get_bestFitnessValue():
            self.set_bestFitnessValue(value)
            self.set_bestStation(station_def_test)
            self.g = g

    # 更新位置
    def update_pos_two(self, part):
        pos_list = []
        for i in range(self.station_count):
            r = random.random()
            pos_value = r*part.get_station_def()[i] + self.get_bestStation()[i]*(1-r)
            pos_list.append((pos_value, i))
        list.sort(pos_list, key=lambda x: x[0], reverse=True)
        sort_index = []
        for ll in self.station_all:
            sort_value = 0
            for l in ll:
                for i in range(self.station_count):
                    if pos_list[i][1] == l:
                        sort_value = sort_value + i
                        break
            sort_index.append(sort_value)
        choose_station = self.station_all[sort_index.index(min(sort_index))]
        g = self.calculate_g(choose_station)
        station_def_test = np.zeros(self.station_count)
        for i in range(self.station_num):
            station_def_test[choose_station[i]] = 1
        part.set_station_def(station_def_test)
        part.set_g(g)
        value = fit_fun(part.get_data(), part.get_station(), part.get_g())
        if value < part.get_fitness_value():
            part.set_fitness_value(value)
            part.set_best_station_def(station_def_test)
        if value < self.get_bestFitnessValue():
            self.set_bestFitnessValue(value)
            self.set_bestStation(station_def_test)
            self.g = g

    def update(self):
        for i in range(self.iter_num):
            for part in self.Particle_list:
                self.update_vel(part)  # 更新速度
                self.update_pos_one(part)
                self.update_pos_two(part)  # 更新位置
            self.fitness_val_list.append(self.get_bestFitnessValue())
            print(self.get_bestStation())  # 每次迭代完把当前的最优适应度存到列表
        return self.fitness_val_list, self.get_bestStation(), self.g

