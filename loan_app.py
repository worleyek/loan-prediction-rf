# imports
import streamlit as st
import pandas as pd
import pickle

# set credit guideline score
credit_guideline = 670

# load model and feature structure
model = pickle.load(open('loan_model.pkl', 'rb'))
model_features = pickle.load(open('model_features.pkl', 'rb'))

# title
st.title("Loan Approval Prediction")
st.write("Fill out the form below to check loan eligibility.")

# user input form
Gender = st.selectbox("Gender", ["Male", "Female"]) # select gender
Married = st.selectbox("Married", ["Yes", "No"]) # select married
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"]) # select dependents
Education = st.selectbox("Education", ["Graduate", "Not Graduate"]) # select education
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"]) # select if self-employed
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"]) # select property area

ApplicantIncome = st.number_input("Total Monthly Income") # applicant income input
CoapplicantIncome = st.number_input("Coapplicant Income (if applicable)") # coapplicant income input

LoanAmount = st.number_input("Loan Amount (in thousands)") # loan amount input
Loan_Amount_Term = st.number_input("Loan Term (months)") # loan term input
credit_score = st.number_input("What is your current credit score?") # get credit score

# determine if person's credit history meets guidelines
# if their credit score is greater than or equal to guideline score
if credit_score >= credit_guideline:
    Credit_History = 1 # yes, their history meets guidelines
else:
    Credit_History = 0 # no, it does not meet guidelines
    

# feature engineering
TotalApplicantIncome = ApplicantIncome + CoapplicantIncome

# create input dataframe

input_dict = {
    'LoanAmount': LoanAmount,
    'Loan_Amount_Term': Loan_Amount_Term,
    'Credit_History': Credit_History,
    'TotalApplicantIncome': TotalApplicantIncome,

    'Gender_Male': 1 if Gender == "Male" else 0,
    'Married_Yes': 1 if Married == "Yes" else 0,
    'Dependents_1': 1 if Dependents == "1" else 0,
    'Dependents_2': 1 if Dependents == "2" else 0,
    'Dependents_3+': 1 if Dependents == "3+" else 0,
    'Education_Not Graduate': 1 if Education == "Not Graduate" else 0,
    'Self_Employed_Yes': 1 if Self_Employed == "Yes" else 0,
    'Property_Area_Semiurban': 1 if Property_Area == "Semiurban" else 0,
    'Property_Area_Urban': 1 if Property_Area == "Urban" else 0
}

input_df = pd.DataFrame([input_dict])

# align with training features
input_df = input_df.reindex(columns=model_features, fill_value=0)

# prediction button
if st.button("Predict Loan Approval"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"Congratulations! You've been pre-approved! (Confidence: {probability:.2%})")
    else:
        st.error(f"We're sorry, but we aren't able to pre-approve you for this loan. (Confidence: {1-probability:.2%})")
