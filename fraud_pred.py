import pandas as pd
from sklearn.ensemble import IsolationForest
df = pd.read_csv("transactions.csv")

features = ["transaction_amount", "transaction_speed", "num_trades_last_24h"]
X = df[features]

model = IsolationForest(n_estimators=100, contamination=0.02)
model.fit(X)

df["fraud_score"] = model.decision_function(X)
df["is_fraudulent"] = model.predict(X)

fraudulent_txns = df[df["is_fraudulent"] == -1]
print(fraudulent_txns)
