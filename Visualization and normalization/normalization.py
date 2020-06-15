# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:33:49 2019

@author: swanuja
"""

from sklearn import preprocessing
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(r'output_final_stdsnormies.csv',encoding='latin-1')

df = pd.read_csv(r'output_final_stdsnormies.csv',encoding='latin-1')

df["views"]=((df["views"]-df["views"].min())/(df["views"].max()-df["views"].min()))*1

print(df["views"])

df["comments"]=((df["comments"]-df["comments"].min())/(df["comments"].max()-df["comments"].min()))*1

print(df["comments"])

