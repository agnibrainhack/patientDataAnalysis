# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:12:17 2018

@author: hp
"""

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

with open('patientdata_csv.csv', 'r') as f:
    reader = pd.read_csv(f)
    
    num_cols = ['Age',  'Height', 'Weight', 'BMI', 'Pulse', 'BP SYS', 'BP DIA']
    transform =reader[num_cols]
    rect = transform.fillna(transform.mean())
    print(transform)
    x = rect.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled)
    sb.pairplot(df, size = 2)