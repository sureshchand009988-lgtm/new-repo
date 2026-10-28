import streamlit as st
import pandas as pd
import numpy as np

col3,col4 = st.columns(2)
with col3:
    st.title("Credit Card Fraud Detection")
with col4:
    st.image("https://static.vecteezy.com/system/resources/previews/009/338/810/original/3d-illustration-credit-card-png.png",width = 150)

button = st.button('🔍 Try prediction')
if(button):
    st.switch_page('pages/prediction.py')
st.markdown('''
### Using Machine Learning to Identify Suspicious Transactions
Credit card fraud is a growing concern in digital payments. This project uses machine learning to distinguish potentially fraudulent transactions from legitimate ones.
Different classification models are trained and evaluated using transaction data, with a focus on precision, recall, F1-score, and ROC-AUC to assess their ability to detect fraud.
Explore the application using the navigation menu above to learn about the dataset, make predictions, and understand the model.
*For educational purposes only. Predictions are estimates and may not always be accurate.*''')



