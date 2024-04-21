import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load training data
train_data = pd.read_csv('diabetes_data.csv')

# Convert last column to integer labels using LabelEncoder
label_encoder = LabelEncoder()
train_data.iloc[:, -1] = label_encoder.fit_transform(train_data.iloc[:, -1])

# Ensure all input features are numeric
train_data.iloc[:, :-1] = train_data.iloc[:, :-1].astype(int)

# List of feature names
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Separate input features (X) and output labels (y) for training data
X = train_data[feature_names]
y = train_data.iloc[:, -1]


# Split the training data into training and testing sets with shuffling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the training features
X_train_scaled = scaler.fit_transform(X_train)

# Transform the testing features using the scaler fitted on the training data
X_test_scaled = scaler.transform(X_test)

# Initialize classifiers
classifiers = {
    'KNN': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(),
    'Logistic Regression': LogisticRegression(),  # Add LogisticRegression
    'nb_classifier': GaussianNB(),
}

# Train classifiers and calculate accuracies
accuracies = {}
for name, clf in classifiers.items():
    clf.fit(X_train_scaled, y_train)  # Use scaled features for training
    y_pred = clf.predict(X_test_scaled)  # Use scaled features for prediction
    accuracy = accuracy_score(y_test, y_pred)
    accuracies[name] = accuracy
    print(f"{name}:{accuracies[name]}")
    
    if accuracies[name]>=0.83:

        # Plot accuracies
        plt.figure(figsize=(12, 6))
        bars = plt.bar(accuracies.keys(), accuracies.values(), color=['blue', 'green', 'red', 'orange', 'purple'])
        plt.xlabel('Classifier')
        plt.ylabel('Accuracy')
        plt.title('Accuracy Comparison of Different Classifiers')
        plt.ylim(0, 1.5)

        # Add percentage labels to bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

        plt.show()
