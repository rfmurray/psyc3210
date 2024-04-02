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
plt.savefig('results_lineplot.png', dpi=300, bbox_inches='tight')
plt.show()

# plot data (bar plot)
sns.set()
sns.barplot(data=df, x='colour', y='height', hue='temperature', ci=95)
plt.savefig('results_barplot.png', dpi=300, bbox_inches='tight')
plt.show()

# run two-way repeated measures anova
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

# find within-subject differences across conditions

# replace columns with differences between columns
df3 = df2.copy()
for i in range(df3.shape[0]):
    df3.iloc[i,:] -= df3.iloc[i,0]

print(df3)

# undo the pivot
df4 = df3.unstack().reset_index()
df4.rename(columns={0:'height'}, inplace=True)
print(df4)

# plot data (line plot, just like above)
sns.pointplot(data=df4, x='colour', y='height', hue='temperature', ci=95)
plt.show()
print(df3)
