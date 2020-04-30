from algorithm.BestPSO import BestPSO
from algorithm.PSO import PSO
from algorithm.BaseAlg import PSOService


class PSOController(object):
    def __init__(self):
        return

    def run(self, data, data_count, station, station_count, station_num, size, count_max, max_vel,
            radius, algorithm,C1, C2):
        if algorithm == 'PSO':
            pso = PSO(data, data_count, station, station_count, station_num, size, count_max, max_vel,
                      radius,C1, C2)
            fit_var_list, best_pos, g = pso.update()
            return fit_var_list, best_pos, g
        elif algorithm == 'BestPSO':
            pso = BestPSO(data, data_count, station, station_count, station_num, size, count_max, max_vel,
                          radius,C1, C2)
            fit_var_list, best_pos, g = pso.update()
            return fit_var_list, best_pos, g

    def calculateCost(self, F, discountRate, payBack, station_num, convertFactor, k, elp, t, fit):
        return PSOService.calculateZ(F, discountRate, payBack, station_num, convertFactor, k, elp, t, fit)

    def calculateBestStationCount(self, k, p, n, S, e, cos):
        return PSOService.calculateBestStationCount(k, p, n, S, e, cos)
