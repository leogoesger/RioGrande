from calculations.ConsumptionEsti import ConsumptionEsti

time_series_file_name = 'TimeSeriesTemperature_florido.csv'
area_file_name = 'Areas.csv'
precipitation_file_name = 'Precipitations.csv'

latitude = 27.14

current_consumption = ConsumptionEsti(time_series_file_name, area_file_name, precipitation_file_name, latitude)
current_consumption.save_to_csv('consumption')
current_consumption.remove_precipitation()
current_consumption.save_to_csv('consumption_without_precipitation')
current_consumption.multiple_of_area()
current_consumption.save_to_csv('consumption_without_precipitation_and_area')
