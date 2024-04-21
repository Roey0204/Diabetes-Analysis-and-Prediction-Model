import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('diabetes_data.csv')

# Exclude the 'Outcome' column
df_features = df.drop(columns=['Outcome'])

# Create a box plot for each feature
plt.figure(figsize=(12, 8))  # Set the size of the plot
sns.boxplot(data=df_features, orient='h', palette='coolwarm')
plt.title('Box Plot for Features (Excluding Outcome)')
plt.xlabel('Value')
plt.ylabel('Feature')
plt.show()
