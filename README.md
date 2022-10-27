# libraries

plotter.py
# Description: code to create majestic plots!
#     script that produces 3 figures: iris_boxplot.png,
#     petal_length_v_width_scatter.png and multi_panel_figure.png
# Usage: python plotter.py

data_processor.py

# Description: contains functions for data processing
# Usage: python data_processor.py {function} {num_rows} {num_columns}
#     {function}: get_random_matrix, get_file_dimensions, or
#               write_matrix_to_file
#     {num_rows}: number of rows desired for matrix
#                 cannot be negative
#     {num_columns}: number of columns desired for matrix
#                    cannot be negative
# Example Call:  python data_processor.py get_file_dimensions


test_hw7.py
# Description: Tests test data_processor.py get_random_matrix,
#              get_file_dimensions and write_matrix_to_file
#             Includes randomness, positive and negative test cases
#             and error cases.
# Usage: python test_hw7.py
