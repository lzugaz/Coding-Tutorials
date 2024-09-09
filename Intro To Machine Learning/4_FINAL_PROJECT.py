"""Project: House Price Prediction
End Goal:
The objective is to build a machine learning model that can predict house prices based on various features, such as the size of the house, number of rooms, and location. By the end of the project, learners will have hands-on experience with data preprocessing, training a model, evaluating it, and visualizing the results.
"""

"""
Project Outline:
1.Introduction:

Explain the problem: predicting house prices using a machine learning model.
Learners will use Linear Regression to predict the price based on a few features.

2.Dataset:

Create or load a dataset with features like house size (in square feet), number of rooms, and location.
If no real dataset is available, create a simple synthetic dataset like this:
size_sqft: The size of the house in square feet.
num_rooms: The number of rooms in the house.
location: A numeric encoding of location types (e.g., 1 = Suburb, 2 = City, 3 = Countryside).
price: The target variable (house price) to be predicted.

3.Data Preprocessing:

Convert the dataset into a format suitable for machine learning.
Handle any missing data, normalize or scale features if necessary.

4.Feature Selection:

Identify the important features that affect house prices the most (size, number of rooms, location, etc.).

5.Train a Model:

Use Linear Regression to train a model that can predict house prices.
Split the dataset into training and testing sets (e.g., 80% training, 20% testing).
Train the model on the training data.

6.Evaluate the Model:

Use performance metrics such as Mean Squared Error (MSE) and R-squared (R²) to evaluate how well the model performs on the test data.

7.Visualize the Results:

Create a scatter plot to compare the actual and predicted prices.
Plot a red diagonal line representing perfect predictions.

8.Conclusion:

Summarize the results and discuss what the learner could do next to improve the model (e.g., adding more features, trying different algorithms).
"""


#START CODE HERE