import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#cleaning
data = pd.read_csv("house-data.csv")
data = data.drop(["date"],axis=1)
data = data.select_dtypes(exclude=["object"])
print(data.isnull().sum())

#corr
c = data.corr()
sns.heatmap(c, annot=True, cmap='coolwarm')
#plt.scatter(data["sqft_living"],data["bedrooms"])
plt.show()