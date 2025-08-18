# salesAnalysis
A comprehensive analysis of sales data provided by a multi-product company, utilizing SQL, Python, and Tableau to provide both descriptive analytics and visualizations.

## Overview
The project takes sales data and performs various functions:
1. Performs data wranglign to eb able to extract various pieces of specific data
2. Create descriptive analytics for the data tha taer visualzied through the use of Tableau
3. Use the sales provided in the table to predict future sales

The final results are:
- A comprehensive Tableau dashboard that includes total sales by category, sales by state of country, most popular products, and more
- Sales trends on a weekly basis with graphs on Tableau
- Predictive analytics on what future sales will be each week moving forward

## Features
- **Data Wrangling**: takes data, cleans it and provides further filters to get relevant data
- **SQL Queries**: queries data to get relevant data taht is used to create visualziation
- **Machine Learning**: predicts next 12 weeks' worth of sales based on data from previous weeks
- **Output Files**: generate CSV fiels with data for each of the SQL queries that are made

## Project Structure

- 'dataWrangling.py' - execute various SQL queries that are used to get tailored data for analysis
- 'salesPrediction.py' - training a ML model that is used to make predictions for sales based on time-series data
- 'train.csv' - data that is origianlly provided from which various insights are drawn

## Setup Instructions

1. Clone repository
2. Ensure to have SQLite installedfor executing SQL queries


## Usage

1. Data wrangling: use dataWrangling.py to clean data and to get various datasets that are saved as CSV files
2. Sales Prediction: to get the prediction for the next 12 weeks for sales for the superstore, run the ML model trained in salesPrediction.py
3. Output: the data wrangling creates various data files that are then used for data visualziation through the Tableau dashboard, and the sales prediction gives the sales for the next 12 weeks as forecasted by the model

## Dependencies
- Python 3.7+
- Pandas
- Numpy
- Scikit-learn
- XGBoost
- SQLite3 

Install dependencies using: 

'''python
pip install pandas numpy scikit-learn xgboost

## Tableau Dashboard

View the interative Tableau dashboard here: https://public.tableau.com/views/Book1_17554446735170/Dashboard3?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link