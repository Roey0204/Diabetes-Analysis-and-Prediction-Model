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

# Create pair plots
pair_plot = sns.pairplot(df_concat, hue='Outcome', palette='coolwarm', diag_kind='kde', height=3)

# Rotate y-axis feature labels by 45 degrees
for ax_row in pair_plot.axes:
    for ax in ax_row:
        ax.set_ylabel(ax.get_ylabel(), rotation=0, ha='right', labelpad=20)  # Rotate labels, adjust alignment, and increase labelpad

# Adjust layout to make space for x-axis labels and long y-axis labels
plt.subplots_adjust(top=0.9, bottom=0.15, left=0.15, right=0.9, hspace=0.4, wspace=0.4)  # Adjust the values as needed

# Adjust figure size to accommodate long labels
plt.gcf().set_size_inches(10, 10)

plt.show()
