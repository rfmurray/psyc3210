# anova_demo.py  Two-way repeated-measures ANOVA

import pandas as pd
from statsmodels.stats.anova import AnovaRM

# read data file into a data frame
df = pd.read_csv('data.csv')
print(df)

# run anova
anova = AnovaRM(data=df, depvar='height', subject='subject',
    within=['colour','temperature'])
result = anova.fit()
print(result)
