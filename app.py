import streamlit as st
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
# col3,col4 = st.columns(2)
# with col3:
#     st.title("Credit Card Fraud Detection")
# with col4:
#     st.image("https://static.vecteezy.com/system/resources/previews/009/338/810/original/3d-illustration-credit-card-png.png",width = 150)
# with open (r"C:\Users\chato\Downloads\credit_card_fraud_detection_model.pkl","rb") as file:
#     model = pickle.load(file)

# col1,col2 = st.columns([2,2])
# with col1:
#     time = st.number_input("enter the Time")
# with col2:
#     amount = st.number_input("enter the Amount")
# l = []
# with st.expander('PCA compnents of the model'):
#     st.write("V1 to V28 are the PCA components which is use in the predict the fraudelent")
#     for i in range(1,29):
#         v = st.number_input(f"PCA components v{i}")
#         l.append(v)
        
# data = np.array([[time] + l + [amount]]).reshape(1,30)
# y_pred = model.predict_proba(data)
# button = st.button("Predict")
# if(button):
#     pred = model.predict(data)
#     prob_1 = y_pred[0][0]
#     prob_2 = y_pred[0][1]
#     if(pred == 1):
#         st.success("✅ Transaction Status: Fraudelent")
#         st.write(f"📊 Probability of Fraud: {prob_2*100 : .1f}%")
#     else:
#          st.success("✅ Transaction Status: Legitimate")
#          st.write(f"📊 Probability of Fraud: {prob_2*100 : .1f}%")
#     if(prob_2 <= 50):
#             st.write("🛡️ Risk Level: Low")
#     elif(prob_2 <= 70):
#             st.write("🛡️ Risk Level: Moderate")
#     else:
#             st.write("🛡️ Risk Level: High")
#     df = pd.DataFrame({'Classes' : ['Legitimate','Fraudelent'],'Probablity' : [prob_1,prob_2]})
#     ax = sns.barplot(data = df, x = 'Classes',y = 'Probablity')
#     st.pyplot(ax.figure)

# with st.expander("About the Model"):
#     st.write('''### 🤖 About the Model
# This application uses a **Random Forest Classifier** to identify potentially fraudulent credit card transactions. The model combines multiple decision trees to analyze transaction patterns and predict whether a transaction is legitimate or fraudulent.
# To handle the imbalance between legitimate and fraudulent transactions, the pipeline incorporates **SMOTE**, which generates synthetic samples of the minority class during training. **StandardScaler** is also included to standardize the input features.
# The model provides a prediction along with estimated probabilities for both classes, helping users understand the model's confidence in its classification.
# **Technologies Used:** Python · Scikit-learn · Random Forest · SMOTE · StandardScaler''')
    
#     st.write("Accuracy",0.9996184843455512*100,"%")
#     st.write("Precision Score of getting a Fraud",  0.94  * 100,"%")
#     st.write("Recall Score of getting a Fraud", 0.79  * 100,"%")
#     st.write("F1_score",0.86*100,"%")
home = st.Page('pages/home.py',title = 'Home')
prediction = st.Page('pages/prediction.py',title = 'Predictor')
about = st.Page('pages/About.py',title = 'About the Model')

pg = st.navigation([home,prediction,about],position = "top")
pg.run()

