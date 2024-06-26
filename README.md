# Diabetes Analysis and Prediction Model

## Sklearn & Matplotlib

This project delves into the realm of machine learning using Python's pandas and matplotlib libraries to thoroughly analyze a diabetes dataset. By harnessing the power of machine learning algorithms, we aim to gain valuable insights and uncover important trends that can aid in making informed decisions and achieving tangible results in healthcare and diagnostics.

With pandas, we efficiently explore and manipulate the dataset, gaining a deep understanding of the features and their relationships. This allows us to preprocess the data and prepare it for model training.

Using various supervised machine learning algorithms such as K-Nearest Neighbors, Decision Trees, Random Forests, Support Vector Machines and Logistic Regression, we delve into predictive modeling. By leveraging different input features related to diabetes risk factors like glucose levels, blood pressure, BMI, and more, we aim to predict the likelihood of a patient having diabetes.

For more details about the supervised algorithm:

1) K-Nearest Neighbors (KNN):
- KNN is a simple, non-parametric algorithm used for classification and regression tasks.
- It works by finding the 'k' nearest data points (neighbors) to a given data point based on a distance metric (usually Euclidean distance).
- For classification, the algorithm assigns the majority class label among its k-nearest neighbors to the query point.
- For regression, the algorithm averages the target values of its k-nearest neighbors to predict the target value for the query point.
KNN does not involve training a model; instead, it directly uses the training data during prediction.

2) Decision Trees:
- Decision Trees are a popular supervised learning algorithm used for both classification and regression tasks.
- The algorithm works by recursively splitting the dataset into subsets based on the feature that best separates the data.
- Each split is chosen to maximize the information gain or minimize impurity (e.g., Gini impurity or entropy).
- Decision Trees are easy to interpret and visualize, making them useful for understanding the decision-making process of the model.
- However, they can be prone to overfitting, especially with complex datasets.

3) Random Forests:
- Random Forests is an ensemble learning technique that builds multiple decision trees and combines their predictions.
- Each decision tree in the ensemble is trained on a random subset of the training data (bagging) and a random subset of the features (feature bagging).
- The final prediction is obtained by aggregating the predictions of all individual trees (e.g., averaging for regression or voting for classification).
- Random Forests are robust to overfitting and generally have higher predictive accuracy compared to individual decision trees.

4) Support Vector Machines (SVM):
- SVM is a powerful supervised learning algorithm used for classification and regression tasks.
- The algorithm works by finding the hyperplane that best separates the data into different classes while maximizing the margin (distance) between the hyperplane and the closest data points (support vectors).
- SVM can handle both linear and nonlinear decision boundaries through the use of kernel functions, which map the data into higher-dimensional feature spaces.
- SVM is effective in high-dimensional spaces and is particularly useful when there is a clear margin of separation between classes.

5) Logistic Regression:
- Despite its name, logistic regression is a linear classification algorithm used for binary classification tasks.
- The algorithm models the probability that a given observation belongs to a particular class using the logistic function (sigmoid function).
- Logistic regression estimates the coefficients of the linear decision boundary between classes, which can be interpreted as the impact of each feature on the log odds of belonging to a certain class.
- It is a simple and interpretable algorithm that is well-suited for binary classification tasks with a linear decision boundary.

<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/img/Supervised%20Learning%20Algorithm.png">
  
Through thorough analysis and experimentation, we evaluate the performance of each algorithm and select the most suitable one based on accuracy and other relevant metrics. By visualizing the results using matplotlib, we present our findings in clear and understandable charts and graphs, enabling stakeholders to grasp the insights derived from the data effortlessly.

Ultimately, this project serves as a testament to the power of machine learning in healthcare, showcasing its ability to analyze vast datasets, extract meaningful patterns, and assist medical professionals in making well-informed decisions for better patient outcomes.

### Box Plot for all input feature
<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/Result/boxplot.png">

#### Comments: 
In the context of the box plot analysis, it has been observed that, apart from the variables 'Glucose' and 'SkinThickness', the distribution of the remaining features exhibits a notable presence of outliers. Outliers, in this context, refer to data points that substantially deviate from the typical range of values observed within the dataset. These outliers may stem from various factors, such as measurement errors, data recording anomalies, or genuine extreme values within the population under study.

These outliers can potentially influence the performance of machine learning models, as they introduce noise and may skew the learned patterns. Consequently, utilizing such unclean data without proper treatment may lead to suboptimal model performance and inaccurate predictions. Therefore, it becomes imperative to address these outliers through appropriate data preprocessing techniques before proceeding with model training.

### Colleration study using Heatmap
<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/Result/heatmap.png">

#### Comments: 
Upon careful observation of the heatmap, it becomes apparent that the correlation coefficients (R-squared values) across each input feature are consistently below the threshold of 0.6. This finding suggests a relatively weak linear relationship between the input features and the target variable.

In statistical analysis, correlation coefficients measure the strength and direction of the linear relationship between two variables. A correlation coefficient closer to 1 indicates a strong positive linear relationship, while a value closer to -1 indicates a strong negative linear relationship. A coefficient near 0 suggests little to no linear relationship between the variables.

When dealing with predictive modeling tasks, having weak correlation coefficients poses challenges for accurately predicting the target variable using linear models. Linear models, such as linear regression rely on strong linear relationships between the input features and the target variable to make accurate predictions. With correlation coefficients below 0.6, the linear models may struggle to capture the underlying patterns and variability in the data, leading to suboptimal predictive performance.

### Distribution Chart agains Outcomes
<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/Result/distribution.png">

#### Comments: 
Upon examining the distribution charts, it becomes evident that the distribution of diabetes outcomes varies across different features such as glucose levels, BMI, and blood pressure values. For features like glucose, BMI, and blood pressure, the distribution appears to be either normal or right-skewed. This indicates that a substantial portion of diabetic patients tends to have higher values for these features, with a significant concentration observed around the central or higher range values.

On the contrary, the distribution of the remaining features exhibits a left-skewed pattern. This suggests that the majority of non-diabetic individuals tend to have lower values for these features, with a smaller proportion exhibiting higher values.

In summary, the distribution patterns provide insights into the relationship between each feature and the occurrence of diabetes. Features such as glucose, BMI, and blood pressure appear to have a notable influence on diabetes outcomes, with higher values often associated with diabetes incidence. Conversely, other features display a different distribution pattern, indicating a potentially different relationship with diabetes risk.

### Visualization Colleration Matrix
<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/Result/pairplot.png">

### Machine Learning Model Accuracy Analysis
<img src="https://github.com/Roey0204/Diabetes-Analysis-and-Prediction-Model/blob/main/Result/Model%20accuracy%20result.png">

#### Comments: 
Upon comparing the performance of various machine learning algorithms, including K-Nearest Neighbors (KNN), Decision Trees, Random Forests, Support Vector Machines (SVM), and Logistic Regression, on our dataset, we found that Logistic Regression yielded the highest accuracy. However, across all models, the average accuracy score was approximately 78%, indicating room for improvement.

Despite achieving a relatively high accuracy, the models still exhibited an average error rate of approximately 22%. This level of error suggests that the models may not generalize well to new data and may benefit from further refinement.

Among the models tested, Logistic Regression emerged as the top performer in terms of accuracy. This indicates that the linear relationship between the input features and the target variable is well-captured by the logistic regression model. However, even with the highest accuracy, there is still a notable margin for improvement to reduce the error rate further.

From my perspective, this analysis highlights the need for additional model tuning, feature engineering, or exploring more sophisticated algorithms to enhance predictive performance. By addressing these areas, we aim to minimize errors and improve the overall robustness and reliability of our predictive models, ultimately leading to better decision-making and outcomes in real-world applications.In addition to the observations made regarding model performance, another perspective to consider is the size of the dataset and its potential impact on our analysis. The relatively small size of our dataset may have limited our ability to effectively identify and capture intricate patterns and relationships within the data.
