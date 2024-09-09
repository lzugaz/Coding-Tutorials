# Step 1: Import necessary libraries (if not already done in previous steps)
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression    
import seaborn as sns            


df = sns.load_dataset('tips')
X = df[['total_bill']] 
y = df['tip']           
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Assuming we have already trained the model and made predictions:
# y_test: The actual values from the test dataset
# y_pred: The predicted values from the model

# Step 2: Evaluate the model using Mean Squared Error (MSE)
# Mean Squared Error calculates the average squared difference between the actual and predicted values.
# A lower MSE value means that the predicted values are close to the actual values.
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 3: Evaluate the model using R-squared (R²)
# R-squared (also called the coefficient of determination) tells us how much of the variance in the target variable (y) 
# can be explained by the features (X). A value closer to 1 means a better fit.
r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

# Step 4: Interpreting the results
# - A low MSE means that the model's predictions are close to the actual values.
# - An R² value close to 1 means that the model is doing a good job of explaining the variance in the target variable.
#   If R² is close to 0, it means that the model is not explaining the data well, and there may be room for improvement.
