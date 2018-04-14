import csv
import numpy as np
from calculations.TW_Consumption import TW_Consumption
from calculations.TW_Constants import TW_Constants
from constant import number_to_month

file_name = 'TimeSeriesTemperature_florido.csv'
latitude = 27.14

with open('raw_files/{}'.format(file_name)) as csvfile:
    current_file = csv.reader(csvfile, delimiter=',')

    # Initial empty matrix and add header column
    consumption_matrix = [['', 'Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
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
                    current_TW_Consumption = TW_Consumption(temperature, month, latitude, const_I, const_a)
                    annual_TW_Consumption.append(round(current_TW_Consumption.consumption, 2))

            # Append consumption array for this year to the matrix
            consumption_matrix.append(annual_TW_Consumption)

np.savetxt("result_files/{}.csv".format(file_name[:-4]), consumption_matrix, delimiter=",", fmt="%s")
