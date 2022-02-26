import pandas as pd
import seaborn as sns

data = pd.read_csv('Country clusters standardized.csv', index_col='Country')
# I indexed the column 'Country' to access and select it to create a dendogram with heatmap.
x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'], axis=1)
# I decided to dropp Language from the dataframe because I won't be using it in this exercise.

sns.clustermap(x_scaled, cmap='vlag')
# I created a dendogram with a heatmap using the Latitude and Longitude of the countries to show their similarities and differences in location.
