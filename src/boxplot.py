import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/roeyy/OneDrive/Desktop/ML-Training/dataset/diabetes_data.csv')

# Exclude the 'Outcome' column
df_features = df.drop(columns=['Outcome'])

# Set up subplots
num_features = len(df_features.columns)
num_rows = 2
num_cols = num_features // 2  # 2 subplots in 1 row
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(16, 12))

# Flatten axes for easy iteration
axes = axes.flatten()

# Define a list of colors for each subplot
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan','grey','yellow']

# Create box plots for each feature
for i, col in enumerate(df_features.columns):
    sns.boxplot(x=df_features[col], ax=axes[i], orient='h', color=colors[i])  # Using different color for each subplot
    axes[i].set_title(f'Box Plot for {col}', fontsize=12)  # Setting font size to 12
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel(None)  # No label for y-axis

# Adjust layout
plt.subplots_adjust(hspace=0.5)  # Increase vertical spacing between subplots
plt.tight_layout()
plt.show()
