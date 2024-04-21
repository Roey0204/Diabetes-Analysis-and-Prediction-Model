import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/roeyy/OneDrive/Desktop/ML-Training/dataset/diabetes_data.csv')

# Extract features (X) and target (y)
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['Outcome']

# Concatenate features and target into one DataFrame
df_concat = pd.concat([X, y], axis=1)

# Set up subplots
num_features = len(X.columns)
num_rows = 4
num_cols = num_features // num_rows + (num_features % num_rows > 0)  # Calculate number of columns dynamically
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(16, 12))

# Flatten axes for easy iteration
axes = axes.flatten()

# Define the color palette for Outcome
palette = {0: 'blue', 1: 'orange'}

# Plot each feature against the outcome
for i, feature in enumerate(X.columns):
    sns.histplot(data=df_concat, x=feature, hue='Outcome', palette=palette, kde=True, alpha=0.5, ax=axes[i])
    axes[i].set_title(f'{feature} vs Outcome')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Frequency')

# Hide empty subplots
for j in range(num_features, num_rows * num_cols):
    axes[j].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()
