# Description: contains functions for data processing
# Usage: python data_processor.py {function} {num_rows} {num_columns}
#     {function}: get_random_matrix, get_file_dimensions, or
#               write_matrix_to_file
#     {num_rows}: number of rows desired for matrix
#     {num_columns}: number of columns desired for matrix
# Example Call:  python data_processor.py get_file_dimensions
import numpy as np
import pandas as pd
import sys


# Description: the following function should create and
# return an N x M matrix of random floating point numbers
# sampled from a unifrom in the range of (0,1]
# num_rows: number of rows, integer > 0
# num_coluns: num of columns, integer > 0
def get_random_matrix(num_rows, num_columns):
    if num_rows > 0 and num_columns > 0:
        rand_mat = np.random.uniform(0, 1, size=(num_rows, num_columns))
        return rand_mat
    return None


# Description: take in name for a comma separated value
# csv file.  Then read in the file and return the dimensions
# of the tabular data (row, columns)
# Example: iris.data should return (150, 5)
def get_file_dimensions(file_name):
    if file_name:
        try:
            file_data = pd.read_csv(file_name, sep=',', header=None)
        except Exception:
            try:
                file_data = pd.read_csv(
                    '../' + file_name, sep=',', header=None)
            except Exception:
                return (0, 0)
        num_rows = len(file_data)
        num_columns = len(file_data.columns)
        return (num_rows, num_columns)
    return (0, 0)


# Description: should create an N x M matrix of random numbers
# from a uniform distribution in the range of (0,1] and then write
# it to a csv file
def write_matrix_to_file(num_rows, num_columns, file_name):
    if file_name and num_rows > 0 and num_columns > 0:
        rand_matrix = get_random_matrix(num_rows, num_columns)
        np.savetxt(file_name, rand_matrix, delimiter=',')
        return 1
    return None


def main():
    option = sys.argv[1]

    if option == "get_random_matrix":
        num_rows = int(sys.argv[2])
        num_columns = int(sys.argv[3])
        rand_mat = get_random_matrix(num_rows, num_columns)
        print(rand_mat)
    elif option == "get_file_dimensions":
        try:
            dimensions = get_file_dimensions('iris.data')
        except Exception:
            dimensions = (get_file_dimensions('../iris.data'))
        print(dimensions)
    elif option == "write_matrix_to_file":
        success = write_matrix_to_file(2, 2, 'test.csv')
        print(success)


if __name__ == '__main__':
    main()
