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

colors = sns.color_palette("colorblind", 4)

# Create subplots with 4 different graphs
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

# Plotting the data for each city
axes[0, 0].plot(pivot_df.index, pivot_df['Dallas'], label='Dallas', marker='o', markersize=5, color=colors[0])
axes[0, 0].set_title('Dallas')
axes[0, 1].plot(pivot_df.index, pivot_df['Denver'], label='Denver', marker='o', markersize=5, color=colors[1])
axes[0, 1].set_title('Denver')
axes[1, 0].plot(pivot_df.index, pivot_df['Oklahoma City'], label='Oklahoma City', marker='o', markersize=5, color=colors[2])
axes[1, 0].set_title('Oklahoma City')
axes[1, 1].plot(pivot_df.index, pivot_df['Seattle'], label='Seattle', marker='o', markersize=5, color=colors[3])
axes[1, 1].set_title('Seattle')

# Adding labels and title to the entire figure
fig.suptitle('Average Temperatures of Four Cities Over Time', fontsize=16)
fig.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust the spacing

# Set y-axis range to start from 0 for all subplots
# for ax in axes.flat:
#     ax.set_ylim(0, None)

# Adding grid lines to all subplots
for ax in axes.flat:
    ax.grid(True, linestyle='--', alpha=0.5)

# Set x-axis ticks at every 10 years for all subplots
# for ax in axes.flat:
#     ax.set_xticks(range(min(pivot_df.index), max(pivot_df.index)+1, 10))

# Show the plot
plt.show()