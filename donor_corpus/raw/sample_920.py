# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:30:46 2020

@author: Aaronga
"""

# Datos faltantes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Tratamiento de los NaN 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3]= imputer.transform(X[:,1:3])
print(X)