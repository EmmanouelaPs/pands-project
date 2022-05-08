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

References used:
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://www.codegrepper.com/code-examples/python/python+download+dataset+from+url
#from sklearn.datasets import load_iris #https://en.wikipedia.org/wiki/Iris_flower_data_set
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
https://www.w3schools.com/python/pandas/pandas_dataframes.asp


Question 2:
I save the above data frame in excel and I add to my repository.

Question 3.1:
I use the decribe function to create a summary statistics of my data and save it to variables_summary.
I'm then importing sys package and I'm saving the file into a writtable text file. After searching, I found out the sdout function (standard output stream) that enables the print function not only to be written to the display but instead to send text to a location called the standard output stream (redirect to a specific file).

References used:
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://stackabuse.com/writing-to-a-file-with-pythons-print-function/

#3.2: Outputs a summary of each variable to a single text file



