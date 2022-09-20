import cmd
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import pickle

# Read student data
d = pd.read_csv("student-data.csv")

data=d.drop(['Roll_number','Name','class'],axis=1)


x=data.iloc[:,:-1]

y=data.iloc[:,27].values

labelencoder_x=LabelEncoder()
x=x.apply(LabelEncoder().fit_transform)
x=x.values

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify = y, test_size=95, random_state=42)

model=DecisionTreeClassifier()
param_dist={"criterion":['gini','entropy'],"max_depth":[1,2,3,4,5]}
grid=GridSearchCV(model,param_grid=param_dist,cv=10,n_jobs=-1)
grid.fit(x_train,y_train)

print("Accuracy of training set",grid.score(x_train,y_train))
print("Accuracy of testing set",grid.score(x_test,y_test))


filename='model.pkl'
pickle.dump(grid,open(filename,'wb'))
load_file=pickle.load(open(filename,'rb'))
print(load_file.predict(x_test))
print(load_file.score(x_test,y_test))
