# plot_demo.py  Show the value of doing a *repeated-measures* ANOVA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create a pattern of differences across conditions that we'll make
# consistent for all simulated subjects
pattern = np.array([0.1, 0.4, 0.2])

# make data for many observers, with large variations across observers,
# but with the pattern we created above across conditions for all observers
offset = np.random.uniform(low=0, high=20, size=(20,1))
data = offset + pattern  # broadcasting!
df = pd.DataFrame(data, columns=['red', 'green', 'blue'])

# unstack
df2 = df.unstack().reset_index()
df2.rename(columns={'level_0': 'colour', 'level_1': 'subject', 0: 'height'}, inplace=True)

# plot the mean and confidence intervals for each category
sns.set()
sns.pointplot(data=df2, x='colour', y='height', ci=95)
plt.show()

# find within-subject differences across conditions
# (don't need to pivot, since we already have df)

# replace columns with differences between columns
df3 = df.copy()
for i in range(df3.shape[0]):
    df3.iloc[i,:] -= df3.iloc[i,0]

print(df3)

# undo the pivot
df4 = df3.unstack().reset_index()
df4.rename(columns={'level_0': 'colour', 'level_1': 'subject', 0: 'height'}, inplace=True)
print(df4)

# plot the mean and confidence intervals for each category
sns.pointplot(data=df4, x='colour', y='height', ci=95)
plt.show()
