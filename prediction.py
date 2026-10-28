import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
col1,col2 = st.columns(2)
with col1:
     st.title("Predictor")
with col2:
     st.image("https://img.lovepik.com/element/45017/8384.png_860.png",width = 150)
st.subheader("It is a predictor which uses a machine learning model to predict the credit card transaction")

with open (r"C:\Users\chato\Downloads\credit_card_fraud_detection_model.pkl","rb") as file:
    model = pickle.load(file)
col1,col2 = st.columns([2,2])
with col1:
    time = st.number_input("enter the Time")
with col2:
    amount = st.number_input("enter the Amount")
l = []
with st.expander('PCA compnents of the model'):
    st.write("V1 to V28 are the PCA components which is use in the predict the fraudelent")
    for i in range(1,29):
        v = st.number_input(f"PCA components v{i}")
        l.append(v)
        
data = np.array([[time] + l + [amount]]).reshape(1,30)
y_pred = model.predict_proba(data)
button = st.button("Predict")
if(button):
    pred = model.predict(data)
    prob_1 = y_pred[0][0]
    prob_2 = y_pred[0][1]
    if(pred == 1):
        st.success("✅ Transaction Status: Fraudelent")
        st.write(f"📊 Probability of Fraud: {prob_2*100 : .1f}%")
    else:
         st.success("✅ Transaction Status: Legitimate")
         st.write(f"📊 Probability of Fraud: {prob_2*100 : .1f}%")
    if(prob_2 <= 50):
            st.write("🛡️ Risk Level: Low")
    elif(prob_2 <= 70):
            st.write("🛡️ Risk Level: Moderate")
    else:
            st.write("🛡️ Risk Level: High")
    fig, ax = plt.subplots()
    df = pd.DataFrame({'Classes' : ['Legitimate','Fraudelent'],'Probablity' : [prob_1,prob_2]})
    ax = sns.barplot(data = df, x = 'Classes',y = 'Probablity')
    #here in this section i use of AI for matching the background
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")
    ax.tick_params(colors="white")
    ax.tick_params(colors="white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.set_title("Transaction Probability", color="white")

    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    st.pyplot(ax.figure)