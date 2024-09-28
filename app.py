############################################################
# import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

######################################################################
# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Construct the full path to the pickle file
model_path = os.path.join(current_dir, 'best_xgb.pkl')

# Load the model from the pickle file
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
##################################################################################
# Define helper functions
# Function to make predictions
def predict(data, threshold=0.29):
    probabilities = model.predict_proba(data)[:, 1]  # Probability of class 1
    predictions = (probabilities >= threshold).astype(int)  # Apply threshold to get crisp labels
    return predictions, probabilities

# Function to create an executive summary table
def create_executive_summary(data):
    # Map one-hot encoded columns back to original categorical values
    data['Job'] = data.apply(lambda row: [col.split('_')[1] for col in row.index if col.startswith('job_') and row[col] == 1][0] if any(row[col] == 1 for col in row.index if col.startswith('job_')) else 'Unknown', axis=1)
    data['Marital Status'] = data.apply(lambda row: 'Married' if row['marital_married'] == 1 else 'Single' if row['marital_single'] == 1 else 'Other', axis=1)
    data['Education'] = data.apply(lambda row: [col.split('_')[1] for col in row.index if col.startswith('education_') and row[col] == 1][0] if any(row[col] == 1 for col in row.index if col.startswith('education_')) else 'Unknown', axis=1)
    data['Has Defaulted?'] = data.apply(lambda row: 'No Information' if row['default_unknown'] == 1 else 'No', axis=1)
    data['Previously Subscribed?'] = data.apply(lambda row: 'Yes' if row['poutcome_success'] == 1 else 'No', axis=1)
    data['Contact Quarter'] = data.apply(lambda row: 'Q2' if row['quarter_Q2'] == 1 else 'Q3' if row['quarter_Q3'] == 1 else 'Other', axis=1)
    data['Prediction Outcome'] = data['Prediction'].apply(lambda x: 'Will Subscribe' if x == 1 else 'Will Not Subscribe')
    data['Probability'] = data['Probability'].apply(lambda x: f'High ({x*100:.0f}%)' if x >= 0.8 else f'Medium \
            ({x*100:.0f}%)' if x >= 0.5 else f'Low ({x*100:.0f}%)' if x >= 0.29 else f'Very Low ({x*100:.0f}%)')

    # Select relevant columns for the executive summary
    executive_summary = data[['age', 'Job', 'Marital Status', 'Education', 'Has Defaulted?', 'Previously Subscribed?', 'Contact Quarter', 'Prediction Outcome', 'Probability']]
    executive_summary.rename(columns={'age': 'Age'}, inplace=True)
    
    return executive_summary

def create_final_report(row):
    # Extract the numeric part of the probability
    probability_str = row['Probability']
    probability_num = float(probability_str.split('(')[1].split('%')[0]) / 100
    
    # Determine the tier based on the probability
    if 'High' in probability_str:
        tier = "Tier 1 "
    elif 'Medium' in probability_str:
        tier = "Tier 2 "
    elif 'Low' in probability_str:
        tier = "Tier 3 "
    else:
        tier = "Tier 4"
    
    # Create the report with the specified format
    report = f"""
    **{tier}
    Customer: Subscription Probability {round(probability_num * 100, 1)}%** 

    | **Age** | **Job** | **Marital Status** | **Education** |
    |---------|---------|--------------------|---------------|
    | {row['Age']} | {row['Job']} | {row['Marital Status']} | {row['Education']} |
    | **Previously Subscribed?** | **Has Defaulted?** | **Prediction Outcome** |
    |----------------------------|--------------------|------------------------|
    | {row['Previously Subscribed?']} | {row['Has Defaulted?']} | {row['Prediction Outcome']} |
    """
    return report
##################################################################################

##################################################################################
# set up sidebar and page layout

# Set page configuration
st.set_page_config(page_title="Predicting Term Deposit Subscription", layout="wide")

# Title of the app
st.title("Predicting Term Deposit Subscription using Binary Classification")

# Sidebar for file upload and user guide
st.sidebar.header("Upload File and User Guide")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# User guide
st.sidebar.markdown("""
### User Guide:

This app allows you to predict whether a customer will subscribe to a term deposit based on various demographic, 
behavioral and other features. Follow the steps below to use the app:

1. **Upload a CSV File**:
   - Click on the "Choose a CSV file" button to upload your dataset. The CSV file should contain the necessary features for prediction.
   - If you don't have a CSV file, the app will use a default test dataset.

2. **View Test Data**:
   - Once the file is uploaded, the test data will be displayed. This includes all the columns from your dataset.

3. **Make Predictions**:
   - The app will automatically make predictions using the pre-trained model. The predictions and probabilities will be added to the dataset.

4. **View Result Table**:
   - The result table will display all columns from the test data along with the prediction labels and probabilities.

5. **View Executive Summary**:
   - The executive summary provides a concise overview of the predictions. It includes key features such as age, job, marital status, education, and the probability of subscription.

6. **Generate Final Report for Selected Customer**:
   - Use the number input to select a specific row index.
   - The final report for the selected customer will be displayed. This report includes:
     - **Tier**: Classification based on the probability of subscription.
     - **Customer: Subscription Probability**: The probability of subscription, displayed in bold.
     - **Age, Job, Marital Status, Education**: Key features displayed in a table format.
     - **Previously Subscribed?, Has Defaulted?, Prediction Outcome**: Additional details displayed in a table format.
""")
##################################################################################
# Main panel for displaying test data and results
if uploaded_file is not None:
    # Read the uploaded file
    test_data = pd.read_csv(uploaded_file)
else:
    st.write("You are using default test data.")
    uploaded_file = os.path.join(current_dir, 'clean_test_data.csv')
    test_data = pd.read_csv(uploaded_file)

    
    # Display test data
    st.subheader("Test Data Set")
    st.write(test_data)
    
    # Make predictions
    predictions, probabilities = predict(test_data)
    
    # Create a DataFrame for results
    results = test_data.copy()
    results['Prediction'] = predictions
    results['Probability'] = probabilities
    
    # Display the result table with all columns from test data, class labels, and probabilities
    st.subheader("Result with Probability and Prediction Columns")
    st.write(results)
    
    # Create the executive summary table
    executive_summary = create_executive_summary(results)
    
    # Display the executive summary
    st.subheader("Executive Summary (Threshold: 0.29):")
    st.write(executive_summary)
    
    # Display the final report for a selected customer
    row_index = st.number_input("Enter row index to see prediction details", min_value=0, max_value=len(executive_summary)-1, value=0)
    final_report = create_final_report(executive_summary.iloc[row_index])
    st.subheader("Final Report for Selected Customer:")
    st.write(final_report)
