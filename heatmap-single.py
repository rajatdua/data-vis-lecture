import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('./dallas_avgtemp.csv')

# Pivot the DataFrame to get the average temperature for each year
pivot_df = df.pivot(index='year', columns='city', values='avg_temp')

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, cmap='coolwarm')

# Show the plot
plt.show()
