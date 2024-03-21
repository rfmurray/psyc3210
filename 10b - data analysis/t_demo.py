# t_demo.py  Dependent samples t-test

import pandas as pd
from scipy.stats import ttest_rel

# read data file into a data frame
df = pd.read_csv('data.csv')
print(df)

# get measurement 1
s1 = df.loc[ (df['colour']=='red') & (df['temperature']=='cold'), 'height']
print(s1)

# get measurement 2
s2 = df.loc[ (df['colour']=='red') & (df['temperature']=='hot'), 'height']
print(s2)

# run t-test
result = ttest_rel(s1, s2)
print(result)
