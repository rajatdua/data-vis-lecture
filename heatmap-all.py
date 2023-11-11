import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# List of CSV files
csv_files = ['./dallas_avgtemp.csv', './denver_avgtemp.csv', './okc_avgtemp.csv', './seattle_avgtemp.csv']  # replace with your actual file names

# Load the data from the CSV files
dataframes = [pd.read_csv(f) for f in csv_files]

# Concatenate the dataframes
df = pd.concat(dataframes)

# Pivot the DataFrame to get the average temperature for each year
pivot_df = df.pivot(index='year', columns='city', values='avg_temp')

# Create the heatmap with the cubehelix color palette
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, cmap='coolwarm')

# Show the plot
plt.show()
