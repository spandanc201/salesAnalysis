import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
import xgboost as xgb

# load data
df = pd.read_csv("trainingData.csv")

# covert to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# keep only relevant columns
df = df[['Order Date', 'Category', 'Sales']]

# one-hot encode categories
df = pd.get_dummies(df, columns=['Category'], drop_first=True)

# aggregate sales data by the week
df.set_index('Order Date', inplace=True)
weekly_sales = df.resample('W').sum()

# lag features
for lag in range(1, 9):
    weekly_sales[f'lag_{lag}'] = weekly_sales['Sales'].shift(lag)

# creation of rolling mean
weekly_sales['rolling_mean_4'] = weekly_sales['Sales'].shift(1).rolling(window=4).mean()
weekly_sales['rolling_mean_8'] = weekly_sales['Sales'].shift(1).rolling(window=8).mean()

weekly_sales.dropna(inplace=True)

# edit the input and output data to include only relevant data
X = weekly_sales.drop('Sales', axis=1)
y = weekly_sales['Sales']

# split the training data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# train the XGBoost model
model = xgb.XGBRegressor(
    n_estimators=1500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)

# evaluate based on the model that is provided
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100  # in percentage

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.3f}")
print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

# provide forecasts for sales over next 12 weeks
last_week = X.iloc[-1].values.reshape(1, -1)
future_preds = []
weeks_to_forecast = 12

for _ in range(weeks_to_forecast):
    pred = model.predict(last_week)[0]
    future_preds.append(pred)
    
    # Shift lag features for next prediction
    last_week = np.roll(last_week, shift=1)
    last_week[0, 0] = pred 
    # Update rolling mean features
    last_week[0, -2] = np.mean(last_week[0, 0:4])  # rolling_mean_4
    last_week[0, -1] = np.mean(last_week[0, 0:8])  # rolling_mean_8

print(f"Next 12 weeks forecast: {future_preds}")
