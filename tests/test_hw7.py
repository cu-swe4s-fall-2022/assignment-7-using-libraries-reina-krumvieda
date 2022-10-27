# Description: Tests test data_processor.py get_random_matrix,
#              get_file_dimensions and write_matrix_to_file
#             Includes randomness, positive and negative test cases
#             and error cases.
# Usage: python test_hw7.py

import random
import unittest
import sys
import numpy as np

sys.path.append('../')
import data_processor  # nopep8


class TestHw7(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # generate random invalid row/column number
        cls.rand_bad_val = random.randint(-10, -1)
        # generate random valid row number
        cls.rand_row_val = random.randint(1, 10)
        # generate random valid column number
        cls.rand_col_val = random.randint(1, 10)
        # set up file name
        cls.file_name = 'iris.data'
        # test file name
        cls.test_file_name = 'test_file_name'
        # random matrix
        cls.none_mat = None

    @classmethod
    def tearDownClass(cls):
        cls.rand_bad_val = None
        cls.rand_row_val = None
        cls.rand_col_val = None
        cls.file_name = None
        cls.none_mat = None

    def test_get_random_matrix(self):

        # 1. positive assertions with randomness
        self.assertEqual(
            data_processor.get_random_matrix(
                self.rand_bad_val, self.rand_col_val), None)

        # 2. negative assertion with randomness
        rand_mat = np.random.uniform(
            0, 1, size=(self.rand_row_val, self.rand_col_val))

        self.assertNotEqual(data_processor.get_random_matrix(
            self.rand_row_val, self.rand_col_val).any(), None)

        # 3. Error Case (return None)
        try:
            assert data_processor.get_random_matrix(
                self.rand_bad_val, self.rand_bad_val) is not None,\
                "ERROR1: Used Neg Inputs!"
            self.assertEqual(data_processor.get_random_matrix(
                self.rand_bad_val, self.rand_bad_val), None)
        except AssertionError as msg:
            print(msg)

    def test_get_file_dimensions(self):
        # 1. positive assertion
        self.assertEqual(data_processor.get_file_dimensions(self.file_name),
                         (150, 5))

        # 2. negative assertion
        self.assertNotEqual(data_processor.get_file_dimensions(self.file_name),
                            (0, 0))

        # 3. Error Case (return (0,0))
        garbage_file_name = "sudflh.data"
        try:
            assert data_processor.get_file_dimensions(
                garbage_file_name) != (0, 0), "ERROR2: Filename DNE!"
            self.assertEqual(data_processor.get_file_dimensions
                             (self.file_name), (0, 0))
        except AssertionError as msg:
            print(msg)

    def test_write_matrix_to_file(self):

        # 1. positive assertion
        self.assertEqual(data_processor.write_matrix_to_file(
            self.rand_row_val, self.rand_col_val, self.test_file_name), 1)

        # 2. negative assertion
        self.assertNotEqual(data_processor.write_matrix_to_file(
            self.rand_row_val, self.rand_col_val, self.test_file_name), None)

        # 3. Error Case (return None -- used negative inputs)
        try:
            assert data_processor.write_matrix_to_file(
                self.rand_bad_val, self.rand_bad_val,
                self.test_file_name) is not None, "ERROR3: Used Neg Inputs!"
            self.assertEqual(data_processor.write_matrix_to_file(
                self.rand_bad_val, self.rand_bad_val,
                self.test_file_name), None)
        except AssertionError as msg:
            print(msg)


if __name__ == '__main__':
    unittest.main()
