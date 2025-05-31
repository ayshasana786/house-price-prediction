import streamlit as st
import joblib
import numpy as np

st.title("House Price Prediction App")

model = joblib.load('rf_model.pkl')  # load your trained RF model here

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you can enter the input from UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of bathrooms", min_value=0, value=0)
living_area = st.number_input("Living area", min_value=0, value=2000)
condition = st.selectbox("Condition of the house", options=[0, 1, 2, 3, 4, 5], index=3)
no_of_schools = st.number_input("Number of schools nearby", min_value=0, value=0)

st.divider()

X= [[bedrooms, bathrooms, living_area, condition, no_of_schools]]

predict_button=st.button("Predict!")

if predict_button:

    st.balloons()

    X_array = np.array(X)

    prediction=model.predict(X_array)[0]

    st.write(f"Price prediction is {prediction:,.2f}")

else:
    st.write("Please use predict button after entering values")

    














#Order of X ['number of bedrooms', 'number of bathrooms', 'living area',
#       'condition of the house', 'Number of schools nearby']