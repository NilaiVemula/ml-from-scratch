import unittest

import numpy as np

from .multiple_linear_regression import MultipleLinearRegression


class TestMultipleLinearRegression(unittest.TestCase):
    def test_init_and_fit(self):
        x1 = np.array([0, 1.05, 2, 3, 4, 5, 6])
        x2 = np.array([0, 1, 2, 3, 4, 5, 6])
        x3 = np.array([0, 1, 2, 3, 3.95, 5, 6])
        y = np.array([0, 3, 6, 9.1, 11.9, 15, 18])
        model = MultipleLinearRegression(y, x1, x2, x3)
        correct = np.array([[0.02281], [-0.43860], [1.05175], [2.38596]])
        np.testing.assert_array_almost_equal(model.beta_hat, correct, decimal=4)


if __name__ == '__main__':
    unittest.main()
