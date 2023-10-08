import streamlit as st
import joblib
import math
# Load the trained model
model = joblib.load('inventory_forecast.pkl')
st.title('Inventory Demand Forecasting')
# Define the input fields
item_id = st.text_input('Item ID', help='0-3048')
dept_id = st.text_input('Dept ID', help='0-6')
cat_id = st.text_input('Cat ID', help='0-2')
store_id = st.text_input('Store ID', help='0-9')
state_id = st.text_input('State ID', help='0-2')
d = st.text_input('Day', help='1-30')
wday = st.text_input('Weekday', help='1-7')
month = st.text_input('Month', help='1-12')
year = st.text_input('Year', help='YYYY')
sell_price = st.text_input('Sell Price')
sold_lag_1 = st.text_input('Sold Lag 1')
sold_lag_2 = st.text_input('Sold Lag 2')
sold_lag_4 = st.text_input('Sold Lag 4')
sold_lag_8 = st.text_input('Sold Lag 8')

# Create a button to make predictions
if st.button('Predict'):
    # Convert input values to a feature array (modify as needed)
    input_data = [[
        item_id, dept_id, cat_id, store_id, state_id, d, wday, month, year,
        sell_price, sold_lag_1, sold_lag_2, sold_lag_4, sold_lag_8
    ]]
    safety_stock=30
    # Make a prediction
    predicted_sales = model.predict(input_data)[0]
    inventory_needed = predicted_sales + safety_stock
    predicted_sales = math.ceil(predicted_sales)
    # Display the prediction
    st.write(f'Predicted Sales: {predicted_sales}units')
    st.write(f'Inventory Needed: {inventory_needed}units')
