# Multiple Linear Regression

Multiple linear regression extends simple linear regression in one important way. It is used to describe a linear relationship between a dependent, or response, variable, <img src="/multiple_linear_regression/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>, and a series of independent variables, <img src="/multiple_linear_regression/tex/d7a31b451b4a0fbe537a3769cd982ce8.svg?invert_in_darkmode&sanitize=true" align=middle width=85.81623434999999pt height=14.15524440000002pt/>. <img src="/multiple_linear_regression/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> is the number of independent, or predictor, variables we wish to include in our model. If we have <img src="/multiple_linear_regression/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> observations on the <img src="/multiple_linear_regression/tex/6b44835ef9c9df90c1ab13fe002f5bf9.svg?invert_in_darkmode&sanitize=true" align=middle width=37.38576269999999pt height=22.831056599999986pt/> variables (all <img src="/multiple_linear_regression/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> predictors and a constant, or bias, term), the mathematical form of this relationship is:

<p align="center"><img src="/multiple_linear_regression/tex/0b6076c5abd2841ddecdca7a841ac144.svg?invert_in_darkmode&sanitize=true" align=middle width=388.39235325pt height=14.611878599999999pt/></p>

where <img src="/multiple_linear_regression/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/> is the error in the model.

## Explicit Solution

To simplify this notation and make it easier to program, we can re-write this in terms of matrices as:

<p align="center"><img src="/multiple_linear_regression/tex/80781d4d815cdeee671e61d20352f026.svg?invert_in_darkmode&sanitize=true" align=middle width=95.25057795pt height=14.611878599999999pt/></p>

where:

<p align="center"><img src="/multiple_linear_regression/tex/c3154972326b3e581fa63bd2759c157b.svg?invert_in_darkmode&sanitize=true" align=middle width=560.8353745499999pt height=88.76800184999999pt/></p>

In a least-squares optimization, we try to minimize the sum of squared residuals (SSR) by optimizing our selection of <img src="/multiple_linear_regression/tex/885c729678a69db7f085b75c99d92ae2.svg?invert_in_darkmode&sanitize=true" align=middle width=10.16555099999999pt height=22.831056599999986pt/>. This is accomplished by defining our model predictions as:

<p align="center"><img src="/multiple_linear_regression/tex/5336f1eb9958d04f4083a2db8b778101.svg?invert_in_darkmode&sanitize=true" align=middle width=68.8837446pt height=18.9497979pt/></p>

and solving for <img src="/multiple_linear_regression/tex/2012e6a4e80d4d65bda472f3676c43ec.svg?invert_in_darkmode&sanitize=true" align=middle width=10.562281949999988pt height=31.50689519999998pt/> by:

<p align="center"><img src="/multiple_linear_regression/tex/5336f1eb9958d04f4083a2db8b778101.svg?invert_in_darkmode&sanitize=true" align=middle width=68.8837446pt height=18.9497979pt/></p>

<p align="center"><img src="/multiple_linear_regression/tex/2a8a321ca0da042c86b2937e4d407245.svg?invert_in_darkmode&sanitize=true" align=middle width=118.1792601pt height=18.9497979pt/></p>

<p align="center"><img src="/multiple_linear_regression/tex/449c9aee1ca0b1e931d393ed34442582.svg?invert_in_darkmode&sanitize=true" align=middle width=256.92689055pt height=19.8630366pt/></p>

<p align="center"><img src="/multiple_linear_regression/tex/6e9666838b48f31cd0fe2df0854e5488.svg?invert_in_darkmode&sanitize=true" align=middle width=140.91062535pt height=19.8630366pt/></p>

### Alternative Solution

Rather than inverting the matrices above, we can solve for <img src="/multiple_linear_regression/tex/885c729678a69db7f085b75c99d92ae2.svg?invert_in_darkmode&sanitize=true" align=middle width=10.16555099999999pt height=22.831056599999986pt/> by solving a matrix equation using LU decomposition or another method. This is typically more computationally efficient and more precise.

## Iterative Solution

In practice, if <img src="/multiple_linear_regression/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and <img src="/multiple_linear_regression/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> are sufficiently large, then the methods above are inefficient. Matrix operations will be computationally expensive, and storing these large matrices will take up significant memory. To solve this problem, the coefficients can be solved using an iterative solution to minimize the sum of squared residuals.

### Gradient Descent

One classic iterative solution is gradient descent. This procedure involves differentiating the sum of squared residuals and then following the steepest path to a local minima. For this procedure, we must introduce two parameters: the learning rate and the number of epochs.

## Evaluation Metrics

Now that we have solved for our regression coefficients in <img src="/multiple_linear_regression/tex/2012e6a4e80d4d65bda472f3676c43ec.svg?invert_in_darkmode&sanitize=true" align=middle width=10.562281949999988pt height=31.50689519999998pt/>, we can finally evaluate our model by looking at the residuals. 

### Residual Sum of Squares

Since the process above uses an ordinary least squares method to find the coefficients, we are minimizing the **residual sum of squares**. A residual is the difference between the predicted value for an observation, <img src="/multiple_linear_regression/tex/bf3f720ea03933ebb03cf8b4665d42c9.svg?invert_in_darkmode&sanitize=true" align=middle width=232.44748890000002pt height=31.50689519999998pt/>, and its actual value, <img src="/multiple_linear_regression/tex/2b442e3e088d1b744730822d18e7aa21.svg?invert_in_darkmode&sanitize=true" align=middle width=12.710331149999991pt height=14.15524440000002pt/>. Therefore, the residual sum of squares is:
<p align="center"><img src="/multiple_linear_regression/tex/376cdb4f1bdb3489d1004cb4819be450.svg?invert_in_darkmode&sanitize=true" align=middle width=153.3883857pt height=44.89738935pt/></p>

### Mean Squared Error

Mean Squared Error is the average of the squared residual across the dataset. Because this metric is divided by the number of observations, it is easier to compare across models and datasets that may have different numbers of data points.
<p align="center"><img src="/multiple_linear_regression/tex/7e73ddacccaee03390374359a0711774.svg?invert_in_darkmode&sanitize=true" align=middle width=221.9126976pt height=44.89738935pt/></p>


### Root Mean Squared Error

Another commonly used metric is Root Mean Squared Error, which is simply the square root of the above metric. 
<p align="center"><img src="/multiple_linear_regression/tex/984002df30ffafe0563991faa44204a8.svg?invert_in_darkmode&sanitize=true" align=middle width=270.3179424pt height=49.315569599999996pt/></p>


### Mean Absolute Error

While the previously discussed metrics deal with over- or under-estimations by squaring the residual, Mean Absolute Error simply takes the average of the absolute value of all residuals.
<p align="center"><img src="/multiple_linear_regression/tex/0538f363343ab01eea956e7aa9f7ceef.svg?invert_in_darkmode&sanitize=true" align=middle width=157.08633765pt height=44.89738935pt/></p>


### Residual Standard Error

The residual standard error is a metric that adjusts the residual sum of squares for the degrees of freedom, or the number of observations and variables.
<p align="center"><img src="/multiple_linear_regression/tex/1a494a63b2926b401c30b56dcb5b5f39.svg?invert_in_darkmode&sanitize=true" align=middle width=142.0651683pt height=39.452455349999994pt/></p>


### Total Sum of Squares

The total sum of squares for the model describes the total amount of variation in the model.
<p align="center"><img src="/multiple_linear_regression/tex/db7d3c106d69c0eba2b50255bdb14227.svg?invert_in_darkmode&sanitize=true" align=middle width=140.14926255pt height=44.89738935pt/></p>


### <img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/>

<img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/> is known as the coefficient of determination and it describes the amount of total variation that is described by the linear model. RSS describes the amount of variation that is left unexplained by the model, and TSS describes the amount of total variation in the model. Typically, this metric ranges from zero and one, but if the model points in the opposite direction of the true relationship then the <img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/> can be negative.
<p align="center"><img src="/multiple_linear_regression/tex/eb79a38dd77cdb36a1382a005894efc3.svg?invert_in_darkmode&sanitize=true" align=middle width=102.54893549999998pt height=33.62942055pt/></p>


### Adjusted <img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/>

For a multiple linear regression, when you add more predictor variables, more variation in the data is always explained. Adjusted <img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/> deals with this issue by lowering the <img src="/multiple_linear_regression/tex/ee9dc84d168b211ff9f4b354e295af3c.svg?invert_in_darkmode&sanitize=true" align=middle width=19.161017699999988pt height=26.76175259999998pt/> value when there are more degrees of freedom in the model.
<p align="center"><img src="/multiple_linear_regression/tex/239502733b630f26355018ec8d447037.svg?invert_in_darkmode&sanitize=true" align=middle width=338.74328564999996pt height=39.452455349999994pt/></p>


## Sources

Much of this information is adapted from [these Cornell lecture notes](http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf) as well as [Wikipedia](https://en.wikipedia.org/wiki/Ordinary_least_squares). All Python code is mine.
