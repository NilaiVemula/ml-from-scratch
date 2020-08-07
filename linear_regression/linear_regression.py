""" Simple Linear Regression """
import math


class LinearRegression:
    """
    A class to describe a simple linear regression model to describe the relationship between
    an independent variable x and a dependent variable y.
    """

    def __init__(self, x, y):
        """ construct model by taking input data and running fit function

        :param x: all x-values
        :type x: list
        :param y: all y-values corresponding to the x-values
        :type y: list
        """

        # validate that x and y have same length
        if len(x) != len(y):
            raise ValueError('There are {} x observations, and {} y observations. There must be an equal number of x' \
                             'and y observations for a linear regression.'.format(len(x), len(y)))

        # store input data
        self.x = x
        self.y = y
        self.n = len(x)  # number of observations

        # fit data to model and save output as model parameters b0 and b1
        self.b1, self.b0 = self._fit()

        # save predicted values
        self.predictions = [self.predict(x_i) for x_i in self.x]

    @property
    def slope(self):
        """ return slope of the regression (b1)"""
        return self.b1

    @property
    def y_intercept(self):
        """ return y-intercept of the regression (b0)"""
        return self.b0

    def _fit(self):
        """ fit data to linear model

        :return: b1, b0
        :rtype: (float, float)
        """

        # mean of our inputs and outputs
        x_mean = sum(self.x) / len(self.x)
        y_mean = sum(self.y) / len(self.y)

        # calculate the b1 and b0
        numerator = sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(self.x, self.y)])
        denominator = sum([(x_i - x_mean) ** 2 for x_i in self.x])

        try:
            b1 = numerator / denominator
            b0 = y_mean - (b1 * x_mean)
        except ZeroDivisionError:
            # if there is a division by zero error, it is a vertical line
            print('Linear Regression fails. Slope is infinity. y-intercept is None')
            b1 = float("inf")
            b0 = None

        return b1, b0

    def predict(self, x):
        y_hat = self.b0 + self.b1 * x
        return y_hat

    # all properties below are for evaluating error
    @property
    def residuals(self):
        """ return a list of residuals"""
        residuals = [y_i - y_hat_i for y_i, y_hat_i in zip(self.y, self.predictions)]
        return residuals

    @property
    def residual_sum_of_squares(self):
        """ return residual sum of squares for linear model"""
        # use sum+map+lambda to find sum of squares of residuals
        rss = sum(map(lambda i: i ** 2, self.residuals))
        return rss

    @property
    def mean_squared_error(self):
        mse = self.residual_sum_of_squares / self.n
        return mse

    @property
    def root_mean_squared_error(self):
        rmse = math.sqrt(self.mean_squared_error)
        return rmse

    @property
    def mean_absolute_error(self):
        abs_residual_sum = sum([abs(e) for e in self.residuals])
        mae = abs_residual_sum / self.n
        return mae

    @property
    def residual_standard_error(self):
        rse = math.sqrt(self.residual_sum_of_squares / (self.n - 2))
        return rse

    @property
    def total_sum_of_squares(self):
        y_mean = sum(self.y) / len(self.y)
        tss = sum(map(lambda i: i ** 2, [y_i - y_mean for y_i in self.y]))
        return tss

    @property
    def r_squared(self):
        r2 = 1 - (self.residual_sum_of_squares / self.total_sum_of_squares)
        return r2

    @property
    def r(self):
        """ return pearson's correlation coefficient"""

        x_mean = sum(self.x) / len(self.x)
        y_mean = sum(self.y) / len(self.y)

        numerator = sum([(x_i - x_mean) * (y_i - y_mean) for x_i, y_i in zip(self.x, self.y)])
        denominator = math.sqrt(
            sum([(x_i - x_mean) ** 2 for x_i in self.x]) * sum([(y_i - y_mean) ** 2 for y_i in self.y]))

        r = numerator / denominator
        return r

    @property
    def adjusted_r_squared(self):
        k = 1  # number of independent regressors
        adj_r2 = 1 - (((1 - self.r_squared) * (self.n - 1)) / (self.n - k - 1))
        return adj_r2

    # hypothesis testing
    def f_statistic(self, p=0.05):
        f = ((self.total_sum_of_squares - self.residual_sum_of_squares) / p) / (
                    self.residual_sum_of_squares / (self.n - p - 1))
        return f

    def __str__(self):
        """ string representation of model is linear equation"""
        return 'y = {} + {} * x'.format(str(self.b0), str(self.b1))
