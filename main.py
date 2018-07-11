from calculations.ConsumptionEsti import ConsumptionEsti
from constant import latitudes


for location in latitudes:
    time_series_file_name = '{}/TimeSeriesTemperature_{}.csv'.format(
        location, location)
    area_file_name = '{}/Areas.csv'.format(location)
    precipitation_file_name = '{}/Precipitations.csv'.format(location)

    latitude = latitudes[location]

    current_consumption = ConsumptionEsti(
        time_series_file_name, area_file_name, precipitation_file_name, latitude, location)
    current_consumption.save_to_csv('{}_consumption'.format(location))
    current_consumption.remove_precipitation()
    current_consumption.save_to_csv(
        '{}_consumption_without_precipitation'.format(location))
    current_consumption.multiple_of_area()
    current_consumption.save_to_csv(
        '{}_consumption_without_precipitation_and_area'.format(location))
