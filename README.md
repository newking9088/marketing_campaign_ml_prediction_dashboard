# Streamlit Dashboard for Customer Subscription Prediction

## Overview
This dashboard demonstrates CI/CD of model deployment and ensures that the performance does not degrade over time, addressing model drift and other related issues.

## Features
This app allows you to predict whether a customer will subscribe to a term deposit based on various demographic, behavioral, and other features. Follow the steps below to use the app:

### 1. Upload a CSV File
- Click on the "Choose a CSV file" button to upload your dataset. The CSV file should contain the necessary features for prediction.
- If you don't have a CSV file, the app will use a default test dataset.

### 2. View Clean Test Data
- Once the file is uploaded, the test data will be displayed. This includes all the columns from your dataset.

### 3. Make Predictions
- The app will automatically make predictions using the pre-trained model. The predictions and probabilities will be added to the dataset.

### 4. View Result Table
- The result table will display all columns from the test data along with the prediction labels and probabilities.

### 5. View Executive Summary
- The executive summary provides a concise overview of the predictions. It includes key features such as age, job, marital status, education, and the probability of subscription.

### 6. Generate Final Report for Selected Customer
- Use the number input to select a specific row index.
- The final report for the selected customer will be displayed. This report includes:
  - **Tier**: Classification based on the probability of subscription.
  - **Customer Subscription Probability**: The probability of subscription, displayed in bold.
  - **Age, Job, Marital Status, Education**: Key features displayed in a table format.
  - **Previously Subscribed?**, **Has Defaulted?**, **Prediction Outcome**: Additional details displayed in a table format

# Deploying a Streamlit Dashboard to the Cloud

## Key Considerations

### 1. Project Structure
- **Dedicated Repository**: Ensure your dashboard has its own dedicated GitHub repository. This helps in managing dependencies and configurations specific to the dashboard.
- **Correct File Placement**: Place your `config.toml` file in a `.streamlit` directory at the root of your project. This ensures Streamlit can correctly apply your theme and other configurations.
- **Virtual environment**: It's always a best practice to create a virtual environment for each individual project.
  
  Example of my project structure:
  
  marketing_campaign_ml_prediction_dashboard/   -- root directory
├── .streamlit/
│   └── config.toml
├── virtual_env/
│   └── ... (virtual environment files)
├── README.md
├── app.py
├── best_xgb.pkl
├── clean_test_data.csv
├── requirements.txt
└── ...

### 2. Dependencies Management
- **Freeze Dependencies**: Use `pip freeze > requirements.txt` to create a `requirements.txt` file. This ensures all necessary packages are installed in the cloud environment.
- **Virtual Environment**: Create and use a virtual environment to manage dependencies. This helps avoid conflicts and ensures consistency between local and cloud environments.

### 3. File Paths
- **Absolute Paths**: Use absolute paths for file operations to avoid issues with relative paths. You can use `os.path.abspath(__file__)` to get the absolute path of the current file.
- **No Spaces in Folder Names**: Ensure folder names do not contain spaces, as this can cause issues with file paths and configurations.

### 4. Configuration Files
- **config.toml**: Ensure your `config.toml` file is correctly formatted and placed in the `.streamlit` directory. This file should include your theme settings and other configurations.
  ```toml
  [theme]
  base="light"
  primaryColor="#ad200f"
  backgroundColor="#f0f7f3"
  secondaryBackgroundColor="#f5970c"
  textColor="#000000"
  font="sans serif"
  ```

### 5. Local Testing
Thoroughly test your dashboard locally before deploying it to the cloud. This helps in identifying and fixing issues early.

### 6. Cloud Logs
Use the logging features provided by Streamlit Cloud to debug issues that arise after deployment.

### 7. Performance Optimization Caching
Use `st.cache` to cache expensive computations and data loading operations. This improves the performance and responsiveness of your dashboard.
```python
@st.cache
def load_data():
    # Expensive data loading operation
    return data
```


