# House-price-prediction
This project involves predicting the prices of houses based on various factors such as location, size, number of rooms, and other relevant features. The primary goal is to build a machine learning model that accurately estimates house prices using a supervised learning approach. The project is built using Python and utilizes libraries like Pandas, Scikit-learn, and Matplotlib for data preprocessing, model training, and visualization.

## Project Overview

The project uses historical housing data and applies machine learning algorithms to predict the market value of houses. The features used in the model include:
- House size (in square feet)
- Number of bedrooms and bathrooms
- Location and neighborhood
- Year of construction
- Additional attributes like parking, garden, etc.

## Features

- Data Preprocessing:Cleaned and transformed the data to handle missing values, categorical variables, and outliers.
- Exploratory Data Analysis (EDA):Performed EDA to visualize and understand the relationships between different features and house prices.
- Modeling:Implemented regression models such as Linear Regression, Random Forest Regressor, and Gradient Boosting to predict house prices.
- Evaluation: Evaluated the models using performance metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

## Setup
### Requirements (`requirements.txt`):

streamlit
pandas
scikit-learn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nidhidhameliya/house-price-prediction.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
### Running the App:
Run the Streamlit app using:
```bash
streamlit run proj_2.py
```
This will launch the app, allowing users to input house details and predict prices using the Random Forest model.

## Results

- The model's performance can be compared with the baseline model and fine-tuned using hyperparameter optimization.
- Visualizations such as scatter plots and regression lines are provided to showcase how well the model predicts house prices.

You can customize it further depending on the specific details of your project.
