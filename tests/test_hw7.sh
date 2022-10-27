# Description: functional test file that uses Stupid Simple Bash
#     testing framework to test data_processor.py get_random_matrix,
#     get_file_dimensions and write_matrix_to_file
# Usage: bash test_hw7.sh

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run get_random_matrix python ../data_processor.py get_random_matrix 2 2 
# functional test for exit codes
assert_exit_code 0
# functional test for returning matrix
# expecting random float array (not (0,0))
assert_in_stdout [0.

run get_file_dimensions python ../data_processor.py get_file_dimensions
# functional test for exit codes
assert_exit_code 0
# functional test for returning file dimensions of iris.data
# expecting dimensions of (150, 5)
assert_in_stdout 150

run write_matrix_to_file python ../data_processor.py write_matrix_to_file
# functional test for exit codes
assert_exit_code 0
# functional test for returning success value
assert_in_stdout 1

