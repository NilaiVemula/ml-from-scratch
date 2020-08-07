""" Multiple Linear Regression """
import numpy as np


class MultipleLinearRegression:
    """
    A class to describe a multiple linear regression model to explain the relationship between multiple independent
    variables (x_i, x_i+1, ..., x_n) and one dependent variable (y).
    """

    def __init__(self, y, *args):
        """ constructor for multiple linear regression

        :param y: (dependent variable) is a numpy array of size 1 by n (number of observations)
        :type y: np.ndarray
        :param args: each arg is a numpy array of size 1 by n (number of observations). There will be k (number of
        predictor variables) args
        :type args: np.ndarray
        :raise ValueError: input numpy arrays have wrong dimensions
        """

        # validate that x and y have same number of observations
        if y.ndim != 1:
            raise ValueError('y must be 1-dimensional. Instead, it is {}-dimensional'.format(y.ndim))
        for i, arg in enumerate(args):
            if arg.ndim != 1:
                raise ValueError('All x vectors must be 1-dimensional. x_{}  is {}-dimensional'.format(arg.ndim, i))
            if arg.shape != y.shape:
                raise ValueError('There are {} x_{} observations, and {} y observations. There must be an equal number '
                                 'of x and y observations for a linear regression.'.format(arg.shape, i, y.shape))

        # add column of ones to x matrix and store input data
        x = np.array(args).T
        self.n, self.k = x.shape

        self.y = np.reshape(y, (1, y.size)).T
        self.x = np.c_[np.ones(self.n), x]

        # fit data to model and save output as model parameters b0 and b1
        self.beta_hat = np.linalg.inv(self.x.T @ self.x) @ self.x.T @ self.y

        # save predicted values
        self.y_hat = self.x @ self.beta_hat

    def predict(self, x):
        """ predict y with given values of x

        :param x: x is a numpy array of size k (number of predictor variables) by 1
        :type x: np.ndarray
        :return: y
        :rtype: float
        """
        x_new = np.r_[np.zeros((1, 1)), x]
        y = float(x_new.T @ self.beta_hat)
        return y

    @property
    def residuals(self):
        """ residuals for the model: difference between actual and predicted y-values

        :return: residuals (numpy array of size n (number of observations) by 1)
        :rtype: np.ndarray
        """
        return self.y - self.y_hat

    @property
    def residual_sum_of_squares(self) -> float:
        """ return residual sum of squares for linear model"""
        # use sum+map+lambda to find sum of squares of residuals
        rss = np.sum(self.residuals ** 2).item()
        return rss

    @property
    def mean_squared_error(self) -> float:
        mse = self.residual_sum_of_squares / self.n
        return mse

    @property
    def root_mean_squared_error(self) -> float:
        rmse = np.sqrt(self.mean_squared_error)
        return rmse

    @property
    def mean_absolute_error(self) -> float:
        abs_residual_sum = np.sum(np.abs(self.residuals))
        mae = abs_residual_sum / self.n
        return mae

    @property
    def residual_standard_error(self) -> float:
        rse = np.sqrt(self.residual_sum_of_squares / (self.n - self.k - 1))
        return rse

    @property
    def total_sum_of_squares(self) -> float:
        y_mean = np.mean(self.y)
        tss = np.sum((self.y - y_mean) ** 2).item()
        return tss

    @property
    def r_squared(self) -> float:
        r2 = 1 - (self.residual_sum_of_squares / self.total_sum_of_squares)
        return r2

    @property
    def adjusted_r_squared(self) -> float:
        adj_r2 = 1 - (((1 - self.r_squared) * (self.n - 1)) / (self.n - self.k - 1))
        return adj_r2
