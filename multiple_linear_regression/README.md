# Multiple Linear Regression

Multiple linear regression extends simple linear regression in one important way. It is used to describe a linear relationship between a dependent, or response, variable, <img src="/multiple_linear_regression/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>, and a series of independent variables, <img src="/multiple_linear_regression/tex/d7a31b451b4a0fbe537a3769cd982ce8.svg?invert_in_darkmode&sanitize=true" align=middle width=85.81623434999999pt height=14.15524440000002pt/>. <img src="/multiple_linear_regression/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> is the number of independent, or predictor, variables we wish to include in our model. If we have <img src="/multiple_linear_regression/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> observations on the <img src="/multiple_linear_regression/tex/6b44835ef9c9df90c1ab13fe002f5bf9.svg?invert_in_darkmode&sanitize=true" align=middle width=37.38576269999999pt height=22.831056599999986pt/> variables (all <img src="/multiple_linear_regression/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/> predictors and a constant, or bias, term), the mathematical form of this relationship is:

<p align="center"><img src="/multiple_linear_regression/tex/0b6076c5abd2841ddecdca7a841ac144.svg?invert_in_darkmode&sanitize=true" align=middle width=388.39235325pt height=14.611878599999999pt/></p>

where <img src="/multiple_linear_regression/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/> is the error in the model.

To simplify this notation and make it easier to program, we can re-write this in terms of matrices as:

<p align="center"><img src="/multiple_linear_regression/tex/80781d4d815cdeee671e61d20352f026.svg?invert_in_darkmode&sanitize=true" align=middle width=95.25057795pt height=14.611878599999999pt/></p>

where:
 
<p align="center"><img src="/multiple_linear_regression/tex/70ca6ed7eceeabf6f153b919cf062ea1.svg?invert_in_darkmode&sanitize=true" align=middle width=502.3383882pt height=179.71811714999998pt/></p>

In a least-squares optimization, we try to minimize the sum of squared residuals (SSR) by optimizing our selection of <img src="/multiple_linear_regression/tex/885c729678a69db7f085b75c99d92ae2.svg?invert_in_darkmode&sanitize=true" align=middle width=10.16555099999999pt height=22.831056599999986pt/>. This is accomplished by defining our model predictions as:

<p align="center"><img src="/multiple_linear_regression/tex/96e54dbe17640f2cd935fbe6e9ca8852.svg?invert_in_darkmode&sanitize=true" align=middle width=68.8837446pt height=18.9497979pt/></p>

and solving for <img src="/multiple_linear_regression/tex/2012e6a4e80d4d65bda472f3676c43ec.svg?invert_in_darkmode&sanitize=true" align=middle width=10.562281949999988pt height=31.50689519999998pt/> by:

<p align="center"><img src="/multiple_linear_regression/tex/04972c5155b4d7262178e1607ab8c914.svg?invert_in_darkmode&sanitize=true" align=middle width=254.96352255pt height=80.82195825pt/></p>

Finally, we evaluate our model by looking at the residuals.
