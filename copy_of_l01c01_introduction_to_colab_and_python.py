# -*- coding: utf-8 -*-
"""Copy of l01c01_introduction_to_colab_and_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17aJTtnKUM5pLYPS-Y2ovPsDNCvWCWtMt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd. read_csv ('Titanic-Dataset.csv')

titanic_data

titanic_data.head ()

titanic_data.info()

titanic_data.describe ()

import seaborn as sns
sns.heatmap (titanic_data.corr (), cmap="YlGnBu")
plt.show()

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit (n_splits=1, test_size=0.2)
for train_indices, test_indices in split.split(titanic_data, titanic_data[ ["Survived", "Pclass", "Sex"]]):
    strat_train_set= titanic_data.loc [train_indices]
    strat_test_set = titanic_data.loc [test_indices]

strat_test_set

plt.subplot (1,2,1)
strat_train_set ['Survived'].hist ()
strat_train_set ['Pclass'].hist ()
plt.subplot (1,2,2)
strat_test_set ['Survived'].hist ()
strat_test_set ['Pclass'].hist ()
plt.show()

strat_train_set.info()

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

class AgeImputer (BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        imputer=SimpleImputer (strategy="mean")
        X['Age']=imputer.fit_transform(X[['Age']])
        return X

from sklearn.preprocessing import OneHotEncoder

class FeatureEncoder (BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        encoder=OneHotEncoder()
        matrix=encoder.fit_transform(X[['Embarked']]).toarray()

        column_names =["C", "S", "O", "N"]
        for i in range (len(matrix.T)):
            X[column_names[i]]=matrix.T[i]
        matrix=encoder.fit_transform(X[['Sex']]).toarray()

        column_names=["Female", "Male"]
        for i in range (len(matrix.T)):
                      X[column_names[i]]=matrix.T[1]
        return X

class FeatureDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop(["Embarked", "Name", "Ticket", "Cabin", "Sex" "N"],axis=1, errors="ignore")

from sklearn.pipeline import Pipeline

pipeline = Pipeline([("ageimputer", AgeImputer()),
                    ("featureencoder", FeatureEncoder()),
                    ("featuredropper", FeatureDropper())])

strat_train_set=pipeline.fit_transform(strat_train_set)

strat_train_set.info()

# Load X from a file called 'X.csv'
X = pd.read_csv('Titanic-Dataset.csv')

#

# Select only columns with int or float data types
X = X.select_dtypes(include=["int", "float"])

# Extract the target variable
y = strat_train_set['Survived']

# Standardize the features
scaler = StandardScaler()
X_data = scaler.fit_transform(X)

# Convert the target variable to a NumPy array
y_data = y.to_numpy()
from sklearn.preprocessing import StandardScaler

X = X.select_dtypes(include=["int", "float"])
y=strat_train_set['Survived']

scaler=StandardScaler()
X_data=scaler.fit_transform(X)
y_data=y.to_numpy()

X_test = X_test.select_dtypes(include=['number'])
y_test=strat_test_set['Survived']

scaler=StandardScaler()
X_data_test=scaler.fit_transform(X_test)
y_data_test=y_test.to_numpy()

print(X_data_train.head())
print(y_data_train.head())

final_data=pipeline.fit_transform(titanic_data)

final_data

X_final = pd.get_dummies(X_final)
y_final=final_data['Survived']
scaler=StandardScaler()
X_data_final=scaler.fit_transform(X_final)
y_data_final=y_final.to_numpy()

prod_clf=RandomForestClassifier()
param_gird = [
    {"n_estimators": [10, 100, 200, 500], "max_depth": [None, 5, 10]},
]
grid_search=GridSearchCV(prod_clf, param_gird, cv=3, scoring="accuracy", return_train_score=True)
grid_search.fit(X_data_final, y_data_final)

prod_final_clf=grid_search.best_estimator_

titanic_test_data=pd.read_csv("test.csv")

final_test_data=pipeline.fit_transform(titanic_test_data)

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Assuming 'Embarked' and 'Sex' are categorical columns, modify this based on your dataset
categorical_columns = ['Age', 'Sex']

# Separate features and target variable
X_final_test = final_data.drop(['Survived'], axis=1)
y_final_test = final_data['Survived']

# Create a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), X_final_test.select_dtypes(include=['number']).columns),
        ('cat', OneHotEncoder(), categorical_columns)
    ])

# Create a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Fit and transform the data
X_data_final_test = pipeline.fit_transform(X_final_test)

final_df=pd.DataFrame(titanic_test_data['PassengerId'])
final_df.to_csv("gender_submission.csv", index=False)

final_df

import warnings
warnings.filterwarnings("ignore")
res=final_df.to_csv
if(res==0):
  print("so sorry! not Survived")
else:
  print("Survived")



