import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# List of CSV files
csv_files = ['./dallas_avgtemp.csv', './denver_avgtemp.csv', './okc_avgtemp.csv', './seattle_avgtemp.csv']  # replace with your actual file names

# Load the data from the CSV files
dataframes = [pd.read_csv(f) for f in csv_files]

# Concatenate the dataframes
df = pd.concat(dataframes)

# Pivot the DataFrame to get the average temperature for each year
pivot_df = df.pivot(index='year', columns='city', values='avg_temp')

# colors = sns.color_palette("colorblind", 4)
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c']


# Plotting the data
plt.figure(figsize=(15, 6))
plt.plot(pivot_df.index, pivot_df['Dallas'], label='Dallas', marker='o', markersize=3, color=colors[0])
plt.plot(pivot_df.index, pivot_df['Denver'], label='Denver', marker='o', markersize=3, color=colors[2])
plt.plot(pivot_df.index, pivot_df['Oklahoma City'], label='Oklahoma City', marker='o', markersize=3, color=colors[1])
plt.plot(pivot_df.index, pivot_df['Seattle'], label='Seattle', marker='o', markersize=3, color=colors[3])



# Set y-axis range to start from 0
plt.ylim(0, None)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperatures of Four Cities Over Time')
plt.legend()

plt.xticks(range(min(pivot_df.index), max(pivot_df.index)+1, 10))


# Show the plot
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()