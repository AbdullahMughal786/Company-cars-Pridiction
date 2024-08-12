from joblib import load
import streamlit as st
import numpy as np
import pandas as pd

model = load('Final Model.joblib')


st.title('Welcome to the Car prices Prediction.')
st.subheader('Please give us some information about your car.')

petrol = st.radio('Petrol or Diesel:',('Petrol','Diesel'))
if petrol=='Petrol':
    petrol=1
else:
    petrol=0

Min = st.number_input('Min Price (Lakh):')
Max = st.number_input('Max Price (Lakh):')
Range = st.number_input('Range (kmpl):')
CC = st.number_input('CC:')
seats = st.number_input('No. of Seats:')
varients = st.number_input('No. of Varients:')


if (st.button('Predict')):
    arr = np.array([[petrol,Min,Max,Range,CC,seats,varients]])
    arr = pd.DataFrame(arr,columns=['Petrol','Min Price (Lakh)',
                                    'Max Price (Lakh)','Range (kmpl)',
                                    'CC','Seats','Variants'])
    pred = model.predict(arr)
    st.success('The prediction is:')
    st.success(f'Ex Showroom Price: {pred[0][0]}')
    st.success(f'RTO: {pred[0][1]}')
    st.success(f'Insurance: {pred[0][2]}')
    st.success(f'Other: {pred[0][3]}')
    st.success(f'Onroad Price: {pred[0][4]}')