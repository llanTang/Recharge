import random
import math
class PSOService:
    def calculateZ(F, discountRate, payBack, station_num, convertFactor, k, elp, t, fit ):
        return PSOService.calculateZ1(F, discountRate, payBack, station_num) + PSOService.calculateZ2(F, convertFactor,
                                                                                station_num) + PSOService.calculateZ3(k, elp, t,
                                                                                                           fit)

    def calculateZ1(F, discountRate, payBack, station_num):
        return F * (discountRate * (1 + discountRate) ** payBack / (
                (1 + discountRate) ** payBack - 1)) * station_num

    def calculateZ2(F, convertFactor, station_num):
        return F * (1 + convertFactor) * station_num

    def calculateZ3(k, elp, t, fit, c=365):
        return c * k * elp * t * fit * 0.00004

    def calculateBestStationCount(k,p,n,S,e,cos):
        return math.ceil((k*p*n)/(S*e*cos))

class Particle:
    # 初始化
    def __init__(self, data, station, station_def, g,fitnessValue ):
        self.__station = station
        self.__g = g
        self.__data = data
        self.__station_def = station_def
        self.__best_station_def = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 粒子最好的位置
        self.__vel = [random.uniform(-1, 1) for i in range(10)]
        self.__fitnessValue = fitnessValue  # 适应度函数值

    def set_station(self, value):
        self.__station = value

    def get_station(self):
        return self.__station

    def set_g(self, value):
        self.__g = value

    def get_g(self):
        return self.__g

    def set_data(self, value):
        self.__data = value

    def get_data(self):
        return self.__data

    def set_station_def(self, value):
        self.__station_def = value

    def get_station_def(self):
        return self.__station_def

    def set_best_station_def(self, value):
        self.__best_station_def = value

    def get_best_station_def(self):
        return self.__best_station_def

    def set_fitness_value(self, value):
        self.__fitnessValue = value

    def get_fitness_value(self):
        return self.__fitnessValue

    def set_vel(self, i, value):
        self.__vel[i] = value

    def get_vel(self):
        return self.__vel