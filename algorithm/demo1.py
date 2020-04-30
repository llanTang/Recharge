import matplotlib.pyplot as plt
import numpy as np
from algorithm.PSO import PSO
from algorithm.BestPSO import BestPSO

dim = 2
size = 5
iter_num = 50
best_position_count = 5
max_vel = 1
data = np.array([[1.4, 2.08, 114],
                 [0.81, 2.33, 121],
                 [1.14, 3.42, 120],
                 [-0.22, 0.72, 237],
                 [2.31, 1.25, 130],
                 [-0.53, 1.91, 112],
                 [1.62, 1.44, 130],
                 [0.81, 1.31, 108],
                 [2.03, 1.02, 123],
                 [0.06, 3.41, 79],
                 [-0.15, 2.81, 118],
                 [2.01, 3.04, 128],
                 [1.91, 3.17, 100],
                 [-0.73, 3.14, 123],
                 [-0.71, 1.75, 100],
                 [0.21, 3.39, 106],
                 [0.55, 1.57, 120],
                 [1.26, 1.73, 75],
                 [1.24, 3.08, 108],
                 [-0.44, 3.92, 105]])

station = np.array([[-0.65, 2.44],
                    [-0.48, 1.46],
                    [0.77, 1.20],
                    [1.80, 2.53],
                    [-0.22, 3.37],
                    [0.70, 1.87],
                    [-0.12, 1.12],
                    [1.86, 1.37],
                    [-0.54, 2.83],
                    [1.65, 3.17]])

pso = PSO(data, 20, station, 10, 5, size, iter_num, max_vel, 2,1.2,1.2)
fit_var_list, best_pos, g = pso.update()

print("最优位置:" + str(best_pos), g)
print("最优解:" + str(fit_var_list[-1]))
plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list, c="R", alpha=0.5)
plt.show()

print("___________")
pso = BestPSO(data, 20, station, 10, 5, size, iter_num, max_vel, 2,1.2,1.2)
fit_var_list, best_pos, g = pso.update()
print("最优位置:" + str(best_pos), g)
print("最优解:" + str(fit_var_list[-1]))
plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list, c="R", alpha=0.5)
plt.show()
