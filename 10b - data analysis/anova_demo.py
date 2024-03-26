# anova_demo.py  Two-way repeated-measures ANOVA

import pandas as pd
from statsmodels.stats.anova import AnovaRM

# read data file into a data frame
df = pd.read_csv('data.csv')
print(df)

# run anova
anova = AnovaRM(data=df, depvar='height', within=['colour','temperature'],
    subject='subject')
result = anova.fit()
print(result)

# first step towards plotting data by category

df2 = df.pivot(index='subject', columns=['colour', 'temperature'], values='height')
print(df2)

mu = df2.mean()
print(mu)

sigma = df2.std()
print(sigma)
