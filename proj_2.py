import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
file_path = 'house_price_prediction_dataset.csv'
data = pd.read_csv(file_path)

# Prepare the features and target variable
X = data.drop('house_price', axis=1)
y = data['house_price']

# Train the model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Streamlit App
st.title('Property Price Prediction')

# User inputs
bedrooms = st.number_input('Enter the number of bedrooms', min_value=1, max_value=10, value=3)
bathrooms = st.number_input('Enter the number of bathrooms', min_value=1, max_value=10, value=2)
sqft_living = st.number_input('Enter the square footage', min_value=500, max_value=10000, value=1500)
lot_size = st.number_input('Enter the lot size', min_value=500, max_value=10000, value=5000)
age = st.number_input('Enter the age of the house', min_value=0, max_value=100, value=20)
proximity_to_city_center = st.number_input('Enter the proximity to city center', min_value=1, max_value=100, value=5)
neighborhood_quality = st.number_input('Enter the neighborhood quality', min_value=1, max_value=10, value=5)

# Prediction
if st.button('Predict House Price'):
    input_data = pd.DataFrame([[bedrooms, bathrooms, sqft_living, lot_size, age, proximity_to_city_center, neighborhood_quality]], 
                              columns=['num_bedrooms', 'num_bathrooms', 'square_footage', 'lot_size', 'age_of_house', 'proximity_to_city_center', 'neighborhood_quality'])
    
    prediction = model.predict(input_data)[0]
    st.write(f'Predicted Property Price: ${prediction:,.2f}')
