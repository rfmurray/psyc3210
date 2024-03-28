# ttest_demo.py  Dependent samples t-test

import pandas as pd
from scipy.stats import ttest_rel

# read data file into a data frame
df = pd.read_csv('data.csv')
print(df)

# version 1

# get measurement 1
s1 = df.loc[ (df['colour']=='red') & (df['temperature']=='cold'), 'height']
print(s1)

# get measurement 2
s2 = df.loc[ (df['colour']=='red') & (df['temperature']=='hot'), 'height']
print(s2)

# run t-test
result = ttest_rel(s1, s2)
print(result)

# version 2

# pivot so that measurements of interest are in columns
df2 = df.pivot(index='subject', columns=['colour', 'temperature'], values='height')
print(df2)

# re-run t-test
x1 = df2[('red','cold')]
x2 = df2[('red','hot')]
result = ttest_rel(x1, x2)
print(result)
