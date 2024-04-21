import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('diabetes_data.csv')

# Extract features (X) and target (y)
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['Outcome']

# Concatenate features and target into one DataFrame
df_concat = pd.concat([X, y], axis=1)

# Calculate correlation matrix
corr_matrix = df_concat.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Rotate x-axis labels
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, ha='right')

# Adjust layout to make space for x-axis labels
plt.subplots_adjust(bottom=0.25, left=0.15, right=0.95, top=0.95)

plt.title('Correlation Heatmap')
plt.show()
