# Step 1: Import necessary libraries
from sklearn.datasets import load_iris  # To load the Iris dataset
from sklearn.model_selection import train_test_split  # To split data into training and testing sets
from sklearn.linear_model import LogisticRegression  # To train a classification model (Logistic Regression)
from sklearn.metrics import accuracy_score, classification_report  # To evaluate the classification model

# Step 2: Load the Iris dataset
# The Iris dataset contains data on three species of Iris flowers (setosa, versicolor, and virginica),
# with features like sepal length, sepal width, petal length, and petal width
iris = load_iris()

# Features (inputs) - Sepal and petal measurements
X = iris.data  # Iris features (input)
# Target (output) - Species of iris flower (setosa, versicolor, virginica)
y = iris.target  # Iris species (output)

# Step 3: Split the dataset into training and testing sets
# 80% of the data will be used for training the model, and 20% for testing it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Initialize and train a Logistic Regression model
# Logistic Regression is commonly used for classification tasks
model = LogisticRegression(max_iter=200)  # Initialize Logistic Regression with a maximum of 200 iterations
model.fit(X_train, y_train)  # Train the model on the training data

# Step 5: Make predictions using the test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model's performance using Accuracy
# Accuracy measures the percentage of correctly classified samples
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")  # Print the accuracy as a percentage

# Step 7: Print a detailed classification report
# This gives more insight into how well the model performs for each class (setosa, versicolor, virginica)
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print("Classification Report:\n", report)

"""
How the code works:
1. The Iris dataset is loaded, and the features and target labels are separated.
2. We split the data into training and testing sets to evaluate the model's performance on unseen data.
3. A Logistic Regression model is trained using the training data.
4. We make predictions using the test data and calculate the accuracy of the model.
5. A classification report is printed, which shows the precision, recall, and F1-score for each species of flower.

How to run the code:
1. Install the required libraries by running:
   pip install scikit-learn
2. Copy this code into a Jupyter Notebook or a Python script.
3. Run the code to see the accuracy and classification report for the Logistic Regression model.

Interactive Exercise:
1. Try changing the test size in the 'train_test_split' function to see how it affects the model's accuracy.
2. Try training the model using different classifiers such as DecisionTreeClassifier, RandomForestClassifier, or SVC (Support Vector Machine).
3. Modify the LogisticRegression parameters, such as 'max_iter' or 'solver', to see if they impact the performance.
"""
