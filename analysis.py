import numpy as np
import pandas as pd

#Question 1: Download the data set and add it to your repository.
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://www.codegrepper.com/code-examples/python/python+download+dataset+from+url


#from sklearn.datasets import load_iris #https://en.wikipedia.org/wiki/Iris_flower_data_set

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
target = iris.target
names = iris.target_names
data = pd.DataFrame(X, columns=iris.feature_names)
data['species'] = iris.target
data['species'] = data['species'].replace(to_replace= [0, 1, 2], value = ['setosa', 'versicolor', 'virginica'])

data.head()

 
file_name = "data.xls" #save data frame as excel file
data.to_excel(file_name) #export data frame to excel file


#Question 2: Download the data set and add it to your repository.
#https://datatofish.com/export-dataframe-to-csv/

file_name = "data.xls" #save data frame as excel file
data.to_excel(file_name) #export data frame to excel file

 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
variables_summary = (data.describe(include='all')) #describe() Function with include=’all’, gives the summary statistics of all the columns.

#Question 3: Write a program called analysis.py that:
#Question 4: Outputs a summary of each variable to a single text file,

import sys #https://stackabuse.com/writing-to-a-file-with-pythons-print-function/


print(variables_summary)
original_stdout = sys.stdout # Save a reference to the original standard output

with open('variables_summary.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(variables_summary)
    sys.stdout = original_stdout # Reset the standard output to its original value

 
#print("columns" , data.columns)

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

plt.hist(Setosa["sepal length (cm)"])
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
plt.savefig('Setosa.png')
plt.close(fig)    # close the figure window

plt.hist(Versicolor["sepal length (cm)"])
plt.show()

plt.hist(Virginica["sepal length (cm)"])
plt.show()

#https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#https://seaborn.pydata.org/generated/seaborn.FacetGrid.html

sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"sepal length (cm)").add_legend()
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"sepal width (cm)").add_legend()
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"petal length (cm)").add_legend()
sns.FacetGrid(data,hue="species",size=5).map(sns.distplot,"petal width (cm)").add_legend()
plt.show()

#https://www.machinelearningplus.com/plots/python-scatter-plot/
 
#create a scatter plot for a pair of variables using scatter on matploiut lib
plt.scatter(x="sepal length (cm)",y="sepal width (cm)",data=data)
plt.show()
#specify only certain variables to include in the pairs plot
sns.pairplot(data[['sepal length (cm)', 'sepal width (cm)']])


#create a pairs plot that colors each point in each plot based on some categorical variable using the hue argument:
sns.pairplot(data, hue='species')
