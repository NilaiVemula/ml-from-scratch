# Multiple Linear Regression

Multiple linear regression extends simple linear regression in one important way. It is used to describe a linear relationship between a dependent, or response, variable, $y$, and a series of independent variables, $x_1, x_2, ..., x_k$. $k$ is the number of independent, or predictor, variables we wish to include in our model. If we have $n$ observations on the $k + 1$ variables (all $k$ predictors and a constant, or bias, term), the mathematical form of this relationship is:

$$
y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \beta_k x_{ik} + \epsilon_i, \hspace{1cm} i=1,...,n
$$

where $\epsilon$ is the error in the model.

To simplify this notation and make it easier to program, we can re-write this in terms of matrices as:
$$
\mathbf{y} = \mathbf{X} \cdot \mathbf{\beta} + \mathbf{\epsilon}
$$
 where:
$$
\mathbf{y} = \begin{bmatrix} y_1\\ 
y_2\\ 
...\\
y_k  
\end{bmatrix}, \hspace{1cm}
\mathbf{X} = \begin{bmatrix} 
1 & x_{11} & x_{12} & ... & x_{1k} \\
1 & x_{21} & x_{22} & ... & x_{2k} \\
1 & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n1} & x_{n2} & ... & x_{nk}
\end{bmatrix} \\
\mathbf{\beta} = \begin{bmatrix} \beta_1\\ 
\beta_2\\ 
...\\
\beta_k  
\end{bmatrix} , \hspace{1cm}
\mathbf{\epsilon} = \begin{bmatrix} \epsilon_1\\ 
\epsilon_2\\ 
...\\
\epsilon_n 
\end{bmatrix}
.
$$

In a least-squares optimization, we try to minimize the sum of squared residuals (SSR) by optimizing our selection of $\mathbf{\beta}$. This is accomplished by defining our model predictions as:
$$
\hat{\mathbf{y}} = \mathbf{X} \cdot \hat{\mathbf{\beta}}\\
$$
and solving for $\hat{\beta}$ by:
$$
\hat{\mathbf{y}} = \mathbf{X} \cdot \hat{\mathbf{\beta}}\\
\mathbf{X}^T \hat{\mathbf{y}} = \mathbf{X}^T \mathbf{X} \cdot \hat{\mathbf{\beta}}\\
(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \hat{\mathbf{y}} = (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \mathbf{X} \cdot \hat{\mathbf{\beta}}\\
(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \hat{\mathbf{y}} = \hat{\mathbf{\beta}}.
$$
Finally, we evaluate our model by looking at the residuals.
$$

$$


