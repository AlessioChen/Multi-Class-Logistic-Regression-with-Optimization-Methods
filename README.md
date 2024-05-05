#  Multi-Class Logstic Regression with Optmization Methods

This repository contains Python code for implementing multi-class logistic regression using gradient descent with Armijo line search and trust region optimization methods with cauchy step. 



## Introduction 
Multi-class logistic regression is a popular technique for classification problems where the target variable can take multiple classes. This repository provides an implementation of multi-class logistic regression along with two optimization methods:

- **Gradient Descent with Armijo Line Search**: This method optimizes the model parameters by iteratively updating them based on the gradient of the loss function, with step size determined using the Armijo line search algorithm.
- **Trust Region Algorithm:**  This method iteratively minimizes the loss function while considering a trust region around the current solution. It utilizes Taylor's second-order model and the Cauchy step to update the model parameters within the trust region.

## Implementation 
The implementation is provided in Python using NumPy for numerical computations. The main components of the implementation include:

- MultiClassLogisticRegression class: Implements multi-class logistic regression with methods for training the model using gradient descent and trust region optimization.
- Functions for computing loss, gradient, Hessian matrix, Armijo line search, and Cauchy step.

## Experimantation 
This repository includes experimentation on a benchmark of multi-class classification datasets. It measures the training loss decrease and runtime for both optimization methods. Additionally, it reports the accuracy of the final model solutions.

## Datasets
Small set of real-world dataset for multi-class classification taska are used. These dataset are directy imported from sklearn datasets or they are download from [LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/) and imported in the datasets directory.


