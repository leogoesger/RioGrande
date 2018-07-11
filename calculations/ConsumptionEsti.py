import csv
import numpy as np
from constant import number_to_month
from utils.helpers import createDataDictionary, get_matrix_without_headers
from calculations.TW_Consumption import TW_Consumption
from calculations.TW_Constants import TW_Constants


class ConsumptionEsti:

    def __init__(self, time_series_file_name, area_file_name, precipitation_file_name, latitude, location):
        self.time_series_file_name = time_series_file_name
        self.consumption_matrix = None
        self.precipitation_dic = createDataDictionary(
            precipitation_file_name)  # Create {year: precipitation}
        self.area_dic = createDataDictionary(
            area_file_name)  # Create {year: area}
        self.latitude = latitude
        self.location = location
        self.const_I = 0
        self.const_a = 0
        self.jennet_factory = 1
        self.get_constants()
        self.get_consumption_matrix()

    def get_constants(self):
        temperature_matrix = get_matrix_without_headers(
            self.time_series_file_name)

        # remove negative temperature values
        for row_index, row in enumerate(temperature_matrix):
            temperature_matrix[row_index] = [0 if i < 0 else i for i in row]

        constants = TW_Constants(
            temperature_matrix, self.latitude, self.location)
        self.const_I = constants.const_I
        self.const_a = constants.const_a
        self.jennet_factory = constants.jennet_factory

    def get_consumption_matrix(self):
        with open('input_files/{}'.format(self.time_series_file_name)) as csvfile:
            current_file = csv.reader(csvfile, delimiter=',')

            # Initial empty matrix and add header column
            self.consumption_matrix = [
                ['', 'Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
            for row_index, row in enumerate(current_file):

                # Omit the first line of meta data for the month
                if row_index != 0:

                    # Calculate TW_Consumption at each individual month by creating an
                    # empty array, then fill the array at each month
                    annual_TW_Consumption = [row[0]]  # header column
                    for i, temp in enumerate(row):

                        if i != 0 and i < 13:  # From first month till 12th month
                            temperature = float(temp)
                            # Omit the first column for meta info
                            month = number_to_month[i - 1]

                            current_TW_Consumption = TW_Consumption(
                                temperature, month, self.latitude, self.const_I, self.const_a)
                            annual_TW_Consumption.append(
                                round(current_TW_Consumption.consumption * self.jennet_factory, 2))

                    # Append consumption array for this year to the matrix
                    self.consumption_matrix.append(annual_TW_Consumption)

    # Account for Precipitation
    # Removing Precipitation from water consumption for each month in each year
    def remove_precipitation(self):
        for row_index, row in enumerate(self.consumption_matrix):
            if row_index != 0 and row[0] in self.precipitation_dic:
                # subtracting precipitation at each month `[i]` for each year `[row[0]]`

                row[1:] = [round(e - self.precipitation_dic[row[0]][i-1]/100, 4)
                           for i, e in enumerate(row) if i > 0]

    # Account for Area Diversion
    # Multiply by area for each month in each year
    def multiple_of_area(self):
        for row_index, row in enumerate(self.consumption_matrix):
            if row_index != 0 and row[0] in self.area_dic:
                row[1:] = [round(e * self.area_dic[row[0]][0]/100000000, 4)
                           for i, e in enumerate(row) if i > 0]

    def save_to_csv(self, name):
        np.savetxt("result_files/{}.csv".format(name),
                   self.consumption_matrix, delimiter=",", fmt="%s")
