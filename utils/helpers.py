import csv


def createDataDictionary(file_name):

    # Create a dictionary
    dictionary = {}

    with open('raw_files/{}'.format(file_name)) as csvfile:
        current_file = csv.reader(csvfile, delimiter=',')

        for row_index, row in enumerate(current_file):
            # Omit the first line of meta data of the file
            if row_index != 0:
                dictionary[row[0]] = [float(i) for i in row[1:]]

    return dictionary


def get_matrix_without_headers(file_name):
    matrix = []
    with open('raw_files/{}'.format(file_name)) as csvfile:
        current_file = csv.reader(csvfile, delimiter=',')
        for row_index, row in enumerate(current_file):
            if row_index != 0:
                matrix.append([float(number) for number in row[1:]])
    return matrix
