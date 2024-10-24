# Streamlit Dashboard for Customer Subscription Prediction

[View Live Dashboard](https://testst-4neyqhlk2bjx6srapde5f9.streamlit.app/)

## Table of Contents
- [Overview](#overview)
- [Dashboard Features](#dashboard-features)
  - [File Upload](#1-upload-a-csv-file)
  - [Data Visualization](#2-view-clean-test-data)
  - [Prediction Engine](#3-make-predictions)
  - [Results Display](#4-view-result-table)
  - [Executive Summary](#5-view-executive-summary)
  - [Customer Reports](#6-generate-final-report-for-selected-customer)
- [Deployment Guide](#deployment-guide)
  - [Project Structure](#1-project-structure)
  - [Dependencies Management](#2-dependencies-management)
  - [Path Configuration](#3-file-paths)
  - [Configuration Setup](#4-configuration-files)
  - [Testing & Optimization](#5-testing-and-optimization)
  - [Monitoring](#6-cloud-monitoring)

## Overview
This dashboard implements CI/CD for model deployment and monitors performance to address model drift and related issues. It provides an interactive interface for predicting customer term deposit subscriptions based on various features.

## Dashboard Features

### 1. Upload a CSV File
- Upload custom dataset via CSV
- Default test dataset available
- Automatic data validation

### 2. View Clean Test Data
- Display processed dataset
- Column overview
- Data quality checks

### 3. Make Predictions
- Automated prediction pipeline
- Pre-trained model integration
- Real-time processing

### 4. View Result Table
- Complete dataset display
- Prediction labels
- Confidence scores

### 5. View Executive Summary
Key metrics displayed:
- Age distribution
- Job categories
- Marital status
- Education levels
- Subscription probabilities

### 6. Generate Final Report for Selected Customer
Detailed customer analysis including:
- **Tier Classification**: Based on subscription probability
- **Customer Profile**:
  - Subscription probability score
  - Demographic information
  - Historical behavior
- **Prediction Details**:
  - Subscription status
  - Default history
  - Previous interactions

## Deployment Guide

### 1. Project Structure
```markdown
marketing_campaign_ml_prediction_dashboard/
├── .streamlit/
│   └── config.toml
├── virtual_env/
├── README.md
├── app.py
├── best_xgb.pkl
├── clean_test_data.csv
└── requirements.txt
```

### 2. Dependencies Management
```bash
# Create virtual environment
python -m venv virtual_env

# Activate environment
source virtual_env/bin/activate  # Unix
virtual_env\Scripts\activate     # Windows

# Generate requirements
pip freeze > requirements.txt
```

### 3. File Paths
```python
# Best practices for file paths
import os
base_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(base_path, 'data')
```

### 4. Configuration Files
```toml
# .streamlit/config.toml
[theme]
base="light"
primaryColor="#ad200f"
backgroundColor="#f0f7f3"
secondaryBackgroundColor="#f5970c"
textColor="#000000"
font="sans serif"
```

### 5. Testing and Optimization
```python
# Performance optimization example
@st.cache
def load_data():
    # Expensive data loading operation
    return data

# Local testing
streamlit run app.py
```

### 6. Cloud Monitoring
- Monitor application logs
- Track performance metrics
- Debug deployment issues
- Implement error handling
