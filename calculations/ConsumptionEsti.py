import csv
import numpy as np
from constant import number_to_month
from utils.helpers import createDataDictionary
from calculations.TW_Consumption import TW_Consumption
from calculations.TW_Constants import TW_Constants

class ConsumptionEsti:

    def __init__(self, time_series_file_name, area_file_name, precipitation_file_name, latitude):
        self.time_series_file_name = time_series_file_name
        self.consumption_matrix = None
        self.precipitation_dic = createDataDictionary(precipitation_file_name)
        self.area_dic = createDataDictionary(area_file_name)
        self.latitude = latitude
        self.get_consumption_matrix()

    def get_consumption_matrix(self):
        with open('raw_files/{}'.format(self.time_series_file_name)) as csvfile:
            current_file = csv.reader(csvfile, delimiter=',')

            # Initial empty matrix and add header column
            self.consumption_matrix = [['', 'Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
            for row_index, row in enumerate(current_file):

                # Omit the first line of meta data for the month
                if row_index != 0:
                    # Calculate TW_Constants based on the entire year's temperature
                    current_TW_Constants = TW_Constants([float(e) for i, e in enumerate(row) if i > 0 ])

                    # Calculate TW_Consumption at each individual month by creating an
                    # empty array, then fill the array at each month
                    annual_TW_Consumption = [row[0]] # header column
                    for i, temp in enumerate(row):

                        if i != 0 and i < 13:
                            temperature = float(temp)
                            month = number_to_month[i - 1] # Omit the first column for meta info
                            const_I = current_TW_Constants.const_I
                            const_a = current_TW_Constants.const_a
                            current_TW_Consumption = TW_Consumption(temperature, month, self.latitude, const_I, const_a)
                            annual_TW_Consumption.append(round(current_TW_Consumption.consumption, 2))

                    # Append consumption array for this year to the matrix
                    self.consumption_matrix.append(annual_TW_Consumption)

    # Account for Precipitation
    def remove_precipitation(self):
        for row_index, row in enumerate(self.consumption_matrix):
            if row_index != 0:
                if row[0] in self.precipitation_dic:
                    row[1:] = [round(e - self.precipitation_dic[row[0]]/100, 2) for i, e in enumerate(row) if i > 0]

    def multiple_of_area(self):
    # Account for Area
        for row_index, row in enumerate(self.consumption_matrix):
            if row_index != 0:
                if row[0] in self.area_dic:
                    row[1:] = [round(e * self.area_dic[row[0]],2) for i, e in enumerate(row) if i > 0]

    def save_to_csv(self, name):
        np.savetxt("result_files/{}.csv".format(name), self.consumption_matrix, delimiter=",", fmt="%s")
