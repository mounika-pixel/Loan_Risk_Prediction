# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd

# # Load the trained model
# model = joblib.load('loan_prediction_model.pkl')

# st.title("Loan Prediction App 💰")
# st.write("Enter the details below to predict if a loan will default.")

# # User Inputs
# credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
# annual_income = st.number_input("Annual Income", min_value=1000, max_value=1000000, value=50000)
# current_loan_amount = st.number_input("Current Loan Amount", min_value=1000, value=10000)
# monthly_debt = st.number_input("Monthly Debt", value=1500.0)
# years_credit_history = st.number_input("Years of Credit History", min_value=0, value=5)
# open_accounts = st.number_input("Number of Open Accounts", min_value=0, value=3)
# max_open_credit = st.number_input("Maximum Open Credit", value=20000.0)
# credit_problems = st.number_input("Number of Credit Problems", min_value=0, value=0)
# bankruptcies = st.number_input("Number of Bankruptcies", min_value=0, value=0)

# # Collect the features into a DataFrame with correct column names
# features = pd.DataFrame(
#     [[credit_score, annual_income, current_loan_amount, monthly_debt,
#       years_credit_history, open_accounts, max_open_credit,
#       credit_problems, bankruptcies]],
#     columns=[
#         'Credit Score', 'Annual Income', 'Current Loan Amount', 'Monthly Debt',
#         'Years of Credit History', 'Number of Open Accounts',
#         'Maximum Open Credit', 'Number of Credit Problems', 'Bankruptcies'
#     ]
# )

# # Predict button
# if st.button("Predict"):
#     prediction = model.predict(features)
#     if prediction[0] == 1:
#         st.error("⚠️ High risk: Likely to default on the loan.")
#     else:
#         st.success("✅ Low risk: Likely to repay the loan.")

# import streamlit as st
# import joblib
# import pandas as pd

# # Load the trained model
# model = joblib.load('loan_prediction_model.pkl')

# # Set page config
# st.set_page_config(page_title="Loan Prediction App", page_icon="💰", layout="centered")

# # Title and Description
# st.markdown("<h1 style='text-align: center; color: teal;'>💳 Loan Prediction</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>Fill in the borrower's information to assess the loan risk.</p>", unsafe_allow_html=True)
# st.write("")

# # Input Fields in 2 columns
# col1, col2 = st.columns(2)

# with col1:
#     credit_score = st.number_input("📈 Credit Score", min_value=300, max_value=850, value=600)
#     annual_income = st.number_input("💼 Annual Income ($)", min_value=1000, max_value=1000000, value=50000)
#     monthly_debt = st.number_input("💸 Monthly Debt ($)", value=1500.0)
#     open_accounts = st.number_input("🔢 Open Accounts", min_value=0, value=3)
#     credit_problems = st.number_input("⚠️ Credit Problems", min_value=0, value=0)

# with col2:
#     current_loan_amount = st.number_input("🏦 Current Loan Amount ($)", min_value=1000, value=10000)
#     years_credit_history = st.number_input("📜 Credit History (Years)", min_value=0, value=5)
#     max_open_credit = st.number_input("💳 Max Open Credit ($)", value=20000.0)
#     bankruptcies = st.number_input("❌ Bankruptcies", min_value=0, value=0)

# # Format input into DataFrame
# features = pd.DataFrame(
#     [[credit_score, annual_income, current_loan_amount, monthly_debt,
#       years_credit_history, open_accounts, max_open_credit,
#       credit_problems, bankruptcies]],
#     columns=[
#         'Credit Score', 'Annual Income', 'Current Loan Amount', 'Monthly Debt',
#         'Years of Credit History', 'Number of Open Accounts',
#         'Maximum Open Credit', 'Number of Credit Problems', 'Bankruptcies'
#     ]
# )

# # Predict
# st.markdown("---")
# if st.button("🔍 Predict Loan Risk"):
#     prediction = model.predict(features)

#     st.markdown("## 🧾 Prediction Result:")
#     if prediction[0] == 1:
#         st.error("⚠️ **High Risk**: This loan is likely to **default**.")
#     else:
#         st.success("✅ **Low Risk**: This loan is likely to be **repaid** on time.")

# # Footer
# st.markdown("---")
# st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

import streamlit as st
import joblib
import pandas as pd
from time import sleep

# Load the trained model
model = joblib.load('loan_prediction_model.pkl')

# Page configuration
st.set_page_config(page_title="Loan Prediction App", page_icon="💰", layout="centered")

# --- Styling: Gradient Heading ---
st.markdown("""
    <style>
        .title {
            background: linear-gradient(to right, #0f2027, #2c5364);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: #888;
        }
        .result {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💳 Loan Risk Prediction App</div>", unsafe_allow_html=True)
st.markdown("<br><p style='text-align: center;'>Enter financial details to predict loan default risk</p>", unsafe_allow_html=True)

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("📈 Credit Score", min_value=300, max_value=850, value=600, help="Higher score means better creditworthiness")
    annual_income = st.number_input("💼 Annual Income ($)", min_value=1000, max_value=1000000, value=50000, help="Your yearly income before tax")
    monthly_debt = st.number_input("💸 Monthly Debt ($)", value=1500.0, help="Total monthly debt payments")
    open_accounts = st.number_input("🔢 Open Accounts", min_value=0, value=3, help="Total number of open credit accounts")
    credit_problems = st.number_input("⚠️ Credit Problems", min_value=0, value=0, help="Number of times you've had credit issues")

with col2:
    current_loan_amount = st.number_input("🏦 Current Loan Amount ($)", min_value=1000, value=10000, help="Amount you are requesting for loan")
    years_credit_history = st.number_input("📜 Credit History (Years)", min_value=0, value=5, help="How long you've had credit")
    max_open_credit = st.number_input("💳 Max Open Credit ($)", value=20000.0, help="Highest amount of open credit available")
    bankruptcies = st.number_input("❌ Bankruptcies", min_value=0, value=0, help="Number of times you've filed for bankruptcy")

# Format input into DataFrame
features = pd.DataFrame(
    [[credit_score, annual_income, current_loan_amount, monthly_debt,
      years_credit_history, open_accounts, max_open_credit,
      credit_problems, bankruptcies]],
    columns=[
        'Credit Score', 'Annual Income', 'Current Loan Amount', 'Monthly Debt',
        'Years of Credit History', 'Number of Open Accounts',
        'Maximum Open Credit', 'Number of Credit Problems', 'Bankruptcies'
    ]
)

# --- Predict ---
st.markdown("---")
if st.button("🔍 Predict Loan Risk"):
    with st.spinner("Analyzing data..."):
        sleep(1)  # Optional fake delay for UX
        prediction = model.predict(features)

    st.markdown("### 🧾 Prediction Result:")
    if prediction[0] == 1:
        st.markdown("<div class='result' style='color: red;'>⚠️ <b>High Risk</b>: This loan is likely to <b>default</b>.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result' style='color: green;'>✅ <b>Low Risk</b>: This loan is likely to be <b>repaid</b> on time.</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <div class='footer'>
        Made with ❤️ using <b>Streamlit</b> & <b>scikit-learn</b> <br>
       
    </div>
""", unsafe_allow_html=True)
