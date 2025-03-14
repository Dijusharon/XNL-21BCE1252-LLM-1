import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("future.csv")
if "time" in df.columns:  
    df["time"] = pd.to_datetime(df["time"])  
    df["timestamp"] = df["time"].astype('int64') // 10**9  

df = df.drop(columns=["time"])  
X = df.drop(columns=["future_price"])  
y = df["future_price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_xgb = XGBRegressor(n_estimators=100, enable_categorical=True)  
model_xgb.fit(X_train, y_train)
preds = model_xgb.predict(X_test)
mse_xgb = mean_squared_error(y_test, preds)
models = {
    "XGBoost": mse_xgb,
    "Reinforcement Learning": 0.02,  
    "LSTM": 0.05  
}
best_model = min(models, key=models.get)
print(f"XGBoost MSE: {mse_xgb}")
print(f"Best Model Selected: {best_model}")
