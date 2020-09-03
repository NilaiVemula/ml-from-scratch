# Multiple Linear Regression

Multiple linear regression extends simple linear regression in one important way. It is used to describe a linear relationship between a dependent, or response, variable, $y$, and a series of independent variables, $x_1, x_2, ..., x_k$. $k$ is the number of independent, or predictor, variables we wish to include in our model. If we have $n$ observations on the $k + 1$ variables (all $k$ predictors and a constant, or bias, term), the mathematical form of this relationship is:

$$
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \beta_k x_{ik} + \epsilon_i, \hspace{1cm} i=1,...,n
$$

where $\epsilon$ is the error in the model.

## Explicit Solution

To simplify this notation and make it easier to program, we can re-write this in terms of matrices as:

$$
\mathbf{y} = \mathbf{X} \cdot \mathbf{\beta} + \mathbf{\epsilon}
$$

where:

$$
\mathbf{y} = \begin{bmatrix} y_1\\ 
y_2\\ 
\vdots\\
y_k  
\end{bmatrix}, \hspace{1cm}
\mathbf{X} = \begin{bmatrix} 
1 & x_{11} & x_{12} & \dots & x_{1k} \\
1 & x_{21} & x_{22} & \dots & x_{2k} \\
1 & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n1} & x_{n2} & \dots & x_{nk}
\end{bmatrix} \\
\mathbf{\beta} = \begin{bmatrix} \beta_1\\ 
\beta_2\\ 
\vdots \\
\beta_k  
\end{bmatrix} , \hspace{1cm}
\mathbf{\epsilon} = \begin{bmatrix} \epsilon_1\\ 
\epsilon_2\\ 
\vdots \\
\epsilon_n 
\end{bmatrix}
.
$$

In a least-squares optimization, we try to minimize the sum of squared residuals (SSR) by optimizing our selection of $\mathbf{\beta}$. This is accomplished by defining our model predictions as:

$$
\hat{\mathbf{y}} = \mathbf{X} \cdot \hat{\mathbf{\beta}}
$$

and solving for $\hat{\beta}$ by:

$$
\hat{\mathbf{y}} = \mathbf{X} \cdot \hat{\mathbf{\beta}}
$$

$$
\mathbf{X}^T \hat{\mathbf{y}} = \mathbf{X}^T \mathbf{X} \cdot \hat{\mathbf{\beta}}
$$

$$
(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \hat{\mathbf{y}} = (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \mathbf{X} \cdot \hat{\mathbf{\beta}}
$$

$$
(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \hat{\mathbf{y}} = \hat{\mathbf{\beta}}.
$$

### Alternative Solution

Rather than inverting the matrices above, we can solve for $\mathbf{\beta}$ by solving a matrix equation using LU decomposition or another method. This is typically more computationally efficient and more precise.

## Iterative Solution

In practice, if $n$ and $k$ are sufficiently large, then the methods above are inefficient. Matrix operations will be computationally expensive, and storing these large matrices will take up significant memory. To solve this problem, the coefficients can be solved using an iterative solution to minimize the sum of squared residuals.

### Gradient Descent

One classic iterative solution is gradient descent. This procedure involves differentiating the sum of squared residuals and then following the steepest path to a local minima. For this procedure, we must introduce two parameters: the learning rate and the number of epochs.

## Evaluation Metrics

Now that we have solved for our regression coefficients in $\hat{\beta}$, we can finally evaluate our model by looking at the residuals. 

### Residual Sum of Squares

Since the process above uses an ordinary least squares method to find the coefficients, we are minimizing the **residual sum of squares**. A residual is the difference between the predicted value for an observation, $\hat{y_i} = \begin{bmatrix} 1 & x_{i1} & x_{i2} & \dots & x_{ik}  \end{bmatrix} \cdot \hat{\beta}$, and its actual value, $y_i$. Therefore, the residual sum of squares is:
$$
\mathrm{RSS}=\sum_{i=1}^{n}\left(y_{i}-\hat{y_i}\right)^{2}.
$$

### Mean Squared Error

Mean Squared Error is the average of the squared residual across the dataset. Because this metric is divided by the number of observations, it is easier to compare across models and datasets that may have different numbers of data points.
$$
\mathrm{MSE}=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y_i}\right)^{2} = \frac{\mathrm{RSS}}{n}
$$


### Root Mean Squared Error

Another commonly used metric is Root Mean Squared Error, which is simply the square root of the above metric. 
$$
\mathrm{RMSE}= \sqrt {\frac{\sum_{i=1}^{n}\left(y_{i}-\hat{y_i}\right)^{2}}{n} } = \sqrt{\mathrm{MSE}}
$$


### Mean Absolute Error

While the previously discussed metrics deal with over- or under-estimations by squaring the residual, Mean Absolute Error simply takes the average of the absolute value of all residuals.
$$
\mathrm{MAE} = \frac{1}{n} \sum_{i=1}^{n}\lvert{y_{i}-\hat{y_i}}\rvert
$$


### Residual Standard Error

The residual standard error is a metric that adjusts the residual sum of squares for the degrees of freedom, or the number of observations and variables.
$$
\mathrm{RSE} = \sqrt{\frac{\mathrm{RSS}}{n-k-1}}
$$


### Total Sum of Squares

The total sum of squares for the model describes the total amount of variation in the model.
$$
\mathrm{TSS}=\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}
$$


### $R^2$

$R^2$ is known as the coefficient of determination and it describes the amount of total variation that is described by the linear model. RSS describes the amount of variation that is left unexplained by the model, and TSS describes the amount of total variation in the model. Typically, this metric ranges from zero and one, but if the model points in the opposite direction of the true relationship then the $R^2$ can be negative.
$$
R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}
$$


### Adjusted $R^2$

For a multiple linear regression, when you add more predictor variables, more variation in the data is always explained. Adjusted $R^2$ deals with this issue by lowering the $R^2$ value when there are more degrees of freedom in the model.
$$
\mathrm{Adjusted}\, R^2 = 1 - \left( \left( \frac{n-1}{n-k-1} \right) \times (1-R^2) \right)
$$


## Sources

Much of this information is adapted from [these Cornell lecture notes](http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf) as well as [Wikipedia](https://en.wikipedia.org/wiki/Ordinary_least_squares). All Python code is mine.
