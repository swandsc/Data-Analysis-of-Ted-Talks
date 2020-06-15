# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:47:42 2019

@author: swanuja
"""

#%matplotlib inline
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'output_final.csv',encoding='latin-1')

#sns.distplot(df['views'])

#sns.distplot(df[df['views'] < 12056699]['views'])

#print(df['views'].describe())

#sns.distplot(df['comments'])

#sns.distplot(df[df['comments'] < 2284]['comments'])

#print(df['comments'].describe())

#sns.jointplot(x='views', y='comments', data=df)
