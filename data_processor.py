# remember to import your libraries!
import numpy as np
import pandas as pd


# Description: the following function should create and 
# return an N x M matrix of random floating point numbers 
# sampled from a unifrom in the range of (0,1]
# num_rows: number of rows, integer > 0 
# num_coluns: num of columns, integer > 0
def get_random_matrix(num_rows, num_columns):
    
    if num_rows > 0 and num_columns > 0:
        rand_mat = np.random.uniform(0,1, size=(num_rows, num_columns) )
        return rand_mat
    return None

# Description: take in name for a comma separated value
# csv file.  Then read in the file and return the dimensions
# of the tabular data (row, columns) 
# Example: iris.data should return (150, 5)
def get_file_dimensions(file_name):
    if file_name:
        file_data = pd.read_csv(file_name, sep=',', header = None)
        num_rows = len(file_data)
        num_columns = len(file_data.columns)
        return(num_rows, num_columns)
    return (0,0)

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
    rand_mat = get_random_matrix(2, 2)
    print(rand_mat)
    dimensions = get_file_dimensions('iris.data')
    print(dimensions)
    write_matrix_to_file(2, 2, 'test.csv')

if __name__ == '__main__':
    main()