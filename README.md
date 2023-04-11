# DataScience_project

This repository was created to practice skills in data science field by trying to use dataset from real-world problems and also trying various techniques in machine learing to tackle the problems.  

## Brazil_house_price
This notebook shows how to predict house price in Brazil. The content of this notebook mainly consists of 4 parts which are cleaning data, exploring data, splitting data, and model part. Using data "Brazil Real Estate Listings" from https://www.kaggle.com/datasets/devvret/brazil-real-estate-listings
* Cleaning data: trying to eliminate outliers, leaky features, and low or high cardinality features
* Exploring data: showing Correlation matrix, histogram, and scatter plot
* Splitting data: dealing with numerical and categorical features
* model: using Linear regression and Ridge regression

## Pytorch
This is a folder for practice pytorch framework from creating model to deploying the model.
* **LinearRegression:** This notebook is to try to use torch framework to create linear regression model. (Learn to create training loop and inference in pytorch)
* **Classification:** This notbook consists of binary classification and multiclass classification generated using sklearn lib. It also creates neural network with only linear activation functions and adding some non-linear activation functions. In the last section, multiclass spiral dataset was created and classified with neural network. (Learn to create more complex model and various kind of loss function)
* **ComputerVision:** Fashion MNIST dataset is used in this notebook. First, trying to use only linear and non-linear activation fucntion in neural network to create the model to classify some types of clothes. Then using Convolution Neural Network(CNN) classify the data and compare with other model. (Learn to create training loop when data must be divided into batches)
