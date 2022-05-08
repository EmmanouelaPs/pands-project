import numpy as np
import pandas as pd

#Question 1: Download the data set and add it to your repository.
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://www.codegrepper.com/code-examples/python/python+download+dataset+from+url


#from sklearn.datasets import load_iris #https://en.wikipedia.org/wiki/Iris_flower_data_set

from sklearn.datasets import load_iris #import the iris package
iris = load_iris()
X = iris.data #attribute it to x variable
target = iris.target #attribute target data from iris to target
names = iris.target_names #attribute target_names data from iris to names
data = pd.DataFrame(X, columns=iris.feature_names) #setting my dataframe by using data and feature_names as my parameters)
data['species'] = iris.target #for column species set it to target
data['species'] = data['species'].replace(to_replace= [0, 1, 2], value = ['setosa', 'versicolor', 'virginica']) #replace the numbers with the iris types for species

data.head() #print the first 10 lines to ensure the outcome is as expected

#Question 2: Download the data set and add it to your repository.
#https://datatofish.com/export-dataframe-to-csv/

file_name = "data.xls" #save data frame as excel file
data.to_excel(file_name) #export data frame to excel file

#Question 3: Write a program called analysis.py that:
#3.1 Outputs a summary of each variable to a single text file,

import sys #https://stackabuse.com/writing-to-a-file-with-pythons-print-function/ #import sys package

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
variables_summary = (data.describe(include='all')) #describe() Function with include=’all’, gives the summary statistics of all the columns.

print(variables_summary) #print the file
original_stdout = sys.stdout # Save a reference to the original standard output

with open('variables_summary.txt', 'w') as f: #open the file in writtable format and redirect it to a new text file using stout
    sys.stdout = f # Change the standard output to the file we created.
    print(variables_summary)
    sys.stdout = original_stdout # Reset the standard output to its original value

    
 #3.2 Saves a histogram of each variable to png files

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

Data_indexed = data.set_index(['species']) #create a new data set with species as index
print (Data_indexed)

Setosa = Data_indexed.loc["setosa"] #filter for setosa specie
print(Setosa)  

Versicolor = Data_indexed.loc["versicolor"] #filter for versicolor specie
print(Versicolor) 

Virginica = Data_indexed.loc["virginica"] #filter for virginica specie
print(Virginica)

plt.hist(Setosa["sepal length (cm)"]) #create a histogram for sepal length for Setosa
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.savefig('Setosa.png') #save the histogram as png file 
plt.close(fig)    # close the figure window

plt.hist(Versicolor["sepal length (cm)"]) #create a histogram for sepal length for Versicolor
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.savefig('Versicolor.png') #save the histogram as png file 
plt.close(fig) # close the figure window

plt.hist(Virginica["sepal length (cm)"]) #create a histogram for sepal length for Virginica
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.savefig('Virginica.png') #save the histogram as png file 
plt.close(fig) # close the figure window

#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#https://seaborn.pydata.org/generated/seaborn.FacetGrid.html

#creating histograms using FacetGrid
#It represent levels of a third variable with the hue parameter, which plots different subsets of data in different colors
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"sepal length (cm)").add_legend()  #choosing hue=species for sepal length
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"sepal width (cm)").add_legend() #choosing hue=species for sepal width
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"petal length (cm)").add_legend() #choosing hue=species for petal length
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"petal width (cm)").add_legend() #choosing hue=species for petal width
plt.show()

#https://www.machinelearningplus.com/plots/python-scatter-plot/

# 3.3 Outputs a scatter plot of each pair of variables. 

#create a scatter plot for a pair of variables using scatter on matploiut lib
plt.scatter(x="sepal length (cm)",y="sepal width (cm)",data=data) 
plt.show()

#specify only certain variables to include in the pairs plot
sns.pairplot(data[['sepal length (cm)', 'sepal width (cm)']])

#create a pairs plot that colors each point in each plot based on some categorical variable using the hue argument:
sns.pairplot(data, hue='species')


# 3.4 Outputs a scatter plot of each pair of variables. 

sns.boxplot(x="species",y="sepal length (cm)",data=data) #creating a boxplot for sepal length
plt.show()

sns.boxplot(x="species",y="sepal width (cm)",data=data) #creating a boxplot for sepal width
plt.show()

sns.boxplot(x="species",y="petal length (cm)",data=data) #creating a boxplot for petal length
plt.show()

sns.boxplot(x="species",y="petal width (cm)",data=data) #creating a boxplot for petal width
plt.show()
