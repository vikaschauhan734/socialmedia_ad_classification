# Socialmedia Ad Classification

This GitHub repository contains a project for classifying social media ads based on user data. The project utilizes the "Social_Network_Ads.csv" dataset, which includes five columns: User ID, Gender, Age, Estimated Salary, and Purchased.

## Project Overview

In this project, we perform the following steps:

1. **Data Preprocessing in `notebook.ipynb`**:
   - Import necessary libraries.
   - Load the dataset from the CSV file as a DataFrame.
   - Check for null values and duplicate entries.
   - Visualize the gender distribution in the dataset.
   - Analyze the distribution of gender by purchase.
   - Analyze the distribution of age.
   - Analyze the distribution of age by purchase.
   - Analyze the distribution of age by gender.
   - Analyze the distribution of estimated salary.
   - Analyze the distribution of estimated salary by gender.
   - Analyze the distribution of estimated salary by purchase.
   - Create a scatter plot between age and estimated salary.
   - Perform one-hot encoding of the gender column.
   - Calculate the correlation between independent and dependent variables.
   - Separate features as X and target as y.
   - Split the data into training and testing sets using train_test_split.
   - Standardize the features.

2. **Model Building and Evaluation**:
   - Train a Support Vector Classifier (SVC) model on the dataset.
   - Make predictions on the test set using the trained model.
   - Create a confusion matrix and classification report to evaluate model performance.
   - Compare model performance with and without the gender column and observe that the model without gender performs better.

3. **Model Saving**:
   - Save the trained model and the feature scaler as pickle files (`model.pkl` and `scaler.pkl`, respectively).

4. **Web Application in `app.py`**:
   - Create a Flask web application for making predictions using the saved model and scaler.
   - Implement the following HTML templates in the `templates` directory:
     - `index.html`: The main prediction page.
     - `true.html`: Displayed when the model predicts "Purchased = 1."
     - `false.html`: Displayed when the model predicts "Purchased = 0."

## Usage

To run the Flask web application and make predictions, follow these steps:

1. Clone this repository to your local machine.

2. Install the required libraries by running:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

## Note

This project demonstrates the process of data preprocessing, model training, and building a web application for ad classification.

For any questions or issues, please feel free to open an issue in this repository.