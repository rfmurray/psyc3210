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
