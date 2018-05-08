import numpy as np

from calculations.TW_Consumption import TW_Consumption
from constant import number_to_month, suppose_consumptive_use

# TW_Constant class calculate I and a based for each year
# Input needs to have an array with 12 elements representing each year's temperature

# I = sum(i_j) from Jan to Dec, where i_j = (T_j_1 / 5) ** 1.514
# a = c_1 * I ** 3 - c_2 * I **2 + c_3 * I + c_4
class TW_Constants:
    c_1 = 675e-9
    c_2 = 771e-7
    c_3 = 179e-4
    c_4 = 0.492

    def __init__(self, temperature_matrix, latitude, location):
        self.temperature_matrix = np.matrix(temperature_matrix)
        self.location = location
        self.const_I = 0
        self.const_a = 0
        self.jennet_factory = 0
        self.T_j = []
        self.size = self.temperature_matrix.shape
        self.U_j = []
        self.latitude = latitude
        self.calculate_I()
        self.calculate_a()
        self.calculate_jennet_factory()

    def calculate_I(self):
        for column_index in range(self.size[1]):
            # T_j_1 is the average temp of that month
            self.T_j.append(np.sum(self.temperature_matrix[:,column_index]) / self.size[0])
            i_j = (self.T_j[-1] / 5) ** 1.514
            self.const_I += i_j

    def calculate_a(self):
        self.const_a = self.c_1 * (self.const_I ** 3) - self.c_2 * (self.const_I ** 2) + self.c_3 * self.const_I + self.c_4

    def calculate_jennet_factory(self):
        for index, T_j in enumerate(self.T_j):
            self.U_j.append(TW_Consumption(T_j, number_to_month[index], self.latitude, self.const_I, self.const_a).consumption)

        self.jennet_factory = suppose_consumptive_use[self.location] / sum(self.U_j)
