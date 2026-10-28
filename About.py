import streamlit as st
import pandas as pd
st.markdown('''### 🤖 About the Model
This application uses a **Random Forest Classifier** to identify potentially fraudulent credit card transactions. The model combines multiple decision trees to analyze transaction patterns and predict whether a transaction is legitimate or fraudulent.
To handle the imbalance between legitimate and fraudulent transactions, the pipeline incorporates **SMOTE**, which generates synthetic samples of the minority class during training. **StandardScaler** is also included to standardize the input features.
The model provides a prediction along with estimated probabilities for both classes, helping users understand the model's confidence in its classification.
**Technologies Used:** Python · Scikit-learn · Random Forest · SMOTE · StandardScaler''')
df = pd.DataFrame({"Accurracy" : [f"{99.7}%"],"Precision Score of getting a Fraud" : [f"{94}%"],"Recall Score of getting a Fraud" : [f"{79}%"],"F1_score" : [f"{86}%"]})
st.dataframe(df)