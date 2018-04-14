from constant import thornthwaite_K

# TW_Consumption calculate consumption given month, temperature
# U = 1.6 * k_a * (10 * T_j / const_I) ** const_a
# k_a is an interpolation
class TW_Consumption:
    def __init__(self, temperature, month, latitude, const_I, const_a):
        self.temperature = temperature
        self.month = month
        self.latitude = latitude
        self.const_I = const_I
        self.const_a = const_a
        self.consumption = 0
        self.calculate_consumption()

    def calculate_consumption(self):
        k_a = thornthwaite_K[self.month](self.latitude)
        temp_factor = ( 10 * self.temperature / self.const_I) ** self.const_a
        self.consumption = 1.6 * k_a * temp_factor
