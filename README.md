# pands-project
This repository contains the Project for Programming and Scripting.

The Fisher's Iris Data Set:

Iris is a very popular garden plant, genus of 260-300 in the family of Iridaceae taking it's name from the Greek word for rainbow.

The British statisticial Ronald Fisher first introduced the Iris flower Data Set, in 1936, which consists of 50 samples of three Iris species  (Setosa, Virginica and Versicolor) and measures four features of each sample: the length and the width of sepals and petals in cm. 

Fisher wanted to distinguish the similar species from each other by developing and using a discriminant and cluster analysis. This analysis aims in finding a linear combination of features that relates or distinguishes two or more classes of objects.

This probably is one of the most famous databases, used in data mining, classification and clustering analysis and to to test algorithms.

Question 1:
We start the code by importing pandas and numpy packages.
I searched online and found that I could import the the iris data set from sklearn.datasets. 
I attribute the data in variable x as I will be later using the name data for the final dataframe.
I save the following variables to clean my data:
target: {ndarray, Series} of shape (150,)
names = target_names: list (The names of target classes)
I save my dataframe as data using my x variable and columns as feature_names(The names of the dataset columns.) I attribute the target into the column species of my dataframe and then in species column we are replacing the number with the corresponding iris type.

I print the first 10 rows to make sure my data as are expected and I save the file in excel.
