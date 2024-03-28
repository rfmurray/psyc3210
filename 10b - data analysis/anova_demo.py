# anova_demo.py  Two-way repeated-measures ANOVA

import pandas as pd
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns

# read data file into a data frame
df = pd.read_csv('data.csv')

# plot data (line plot)
sns.set()
sns.pointplot(data=df, x='colour', y='height', hue='temperature', ci=95)
plt.show()

# plot data (bar plot)
sns.set()
sns.barplot(data=df, x='colour', y='height', hue='temperature', ci=95)
plt.show()

# run anova
anova = AnovaRM(data=df, depvar='height', within=['colour','temperature'],
    subject='subject')
result = anova.fit()
print(result)

# get summary data
df2 = df.pivot(index='subject', columns=['colour', 'temperature'], values='height')
mu = df2.mean()
sigma = df2.std()
print(mu)
print(sigma)
