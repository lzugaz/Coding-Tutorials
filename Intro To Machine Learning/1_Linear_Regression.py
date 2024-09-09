# Step 1: Import necessary libraries
# These libraries will help us work with data, build a machine learning model, and visualize the results
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression     # To create a Linear Regression model
from sklearn.metrics import mean_squared_error, r2_score  # For evaluating the model performance
import matplotlib.pyplot as plt  # To create visualizations
import seaborn as sns            # For easier data visualization and handling

# Step 2: Load a sample dataset
# We're using Seaborn's 'tips' dataset which contains information about restaurant bills and tips
# We'll predict the amount of 'tip' based on the 'total_bill'
df = sns.load_dataset('tips')

# Step 3: Preprocess the data
# We need to select the features (inputs) and the target (output) we want to predict
# In this case, our feature is the 'total_bill' and the target is 'tip'
X = df[['total_bill']]  # Features (input)
y = df['tip']           # Target variable (output we want to predict)

# Step 4: Split the dataset into training and testing sets
# We split the data so that we can train the model on one part (training data) and test it on another (test data)
# The 'test_size=0.2' means 20% of the data will be used for testing, and 80% for training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train the Linear Regression model
# We're using a Linear Regression model from Scikit-learn, which assumes a linear relationship between the input and output
model = LinearRegression()
# Train the model on the training data
model.fit(X_train, y_train)

# Step 6: Make predictions
# Once the model is trained, we use it to predict the 'tip' values on the test data
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
# We use Mean Squared Error (MSE) to measure how close the predicted values are to the actual values (lower MSE is better)
# We also use R-squared (R²) to measure how well the model explains the variability of the data (closer to 1 is better)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Step 8: Visualize the results
# Now we create a scatter plot to visually compare the actual 'tip' values with the predicted values
# Blue dots represent the actual tips, and the red line represents the predicted tips based on the total bill
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Total Bill')  # X-axis label
plt.ylabel('Tip Amount')  # Y-axis label
plt.title('Linear Regression: Predicting Tip Amount')  # Plot title
plt.legend()  # Show legend for 'Actual' and 'Predicted'
plt.show()  # Display the plot

print(f"y-test = {y_test}, y pred = {y_pred}")
""" Instructions to run:
Install the required libraries by running:
pip install numpy pandas scikit-learn matplotlib seaborn
Copy the code into a Jupyter Notebook or a Python script, and run it to see the results. """