from transformers import pipeline
nlp_model = pipeline("text-classification", model="roberta-large")

def detect_fraud(transaction_details):
    result = nlp_model(transaction_details)
    return result[0]['label']

transaction_text = "High-speed transaction of $500,000 detected from unknown wallet"
fraud_prediction = detect_fraud(transaction_text)

print(f"Fraud Prediction: {fraud_prediction}")
