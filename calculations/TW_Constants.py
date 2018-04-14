# TW_Constant class calculate I and a based for each year
# Input needs to have an array with 12 elements representing each year's temperature

# I = sum(i_j) from Jan to Dec, where i_j = (T_j / 5) ** 1.514
# a = c_1 * I ** 3 - c_2 * I **2 + c_3 * I + c_4
class TW_Constants:
    c_1 = 657e-9
    c_2 = 771e-7
    c_3 = 170e-4
    c_4 = 0.492

    def __init__(self, temperature_array):
        self.temperature_array = temperature_array
        self.const_I = 0
        self.const_a = 0
        self.calculate_I()
        self.calculate_a()

    def calculate_I(self):
        for temperature in self.temperature_array:
            i_j = (temperature / 5) ** 1.514
            self.const_I += i_j

    def calculate_a(self):
        self.const_a = self.c_1 * self.const_I ** 3 - \
            self.c_2 * self.const_I ** 2 + self.c_3 * self.const_I + self.c_4
