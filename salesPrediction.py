import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import sqlite3
import pandas as pd

df = pd.read_csv("trainingData.csv")

# converting all date column entries to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst = True)

# take only useful features (numeric features) from columns
df['Order_Month'] = df['Order Date'].dt.month
df['Order_Weekday'] = df['Order Date'].dt.weekday

allColumns = ['Order Date', 'Ship Mode', 'Segment', 'Region', 'Category', 'Sales', 'Order_Month', 'Order_Weekday']
df = df[allColumns]

# One-hot encode categorical columns
categorical_cols = ['Ship Mode', 'Segment', 'Region', 'Category']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df_encoded.drop(['Sales', 'Order Date'], axis=1)
y = df_encoded['Sales']

print(X.head())
print(y.head())

