import json
import requests

# Load credentials
with open("E:/Cognitive customer insights/data/ibm_credentials.json") as f:
    creds = json.load(f)

# Function to train AI model
def train_model(data):
    response = requests.post(
        f"{creds['WATSONX_URL']}/v1/train",
        json={"data": data, "model_type": "classification"},
        headers={"Authorization": f"Bearer {creds['WATSONX_API_KEY']}"}
    )
    return response.json()

# Load processed data
with open("E:/Cognitive customer insights/data/processed_reviews.csv") as f:
    data = f.read()

# Train model
model_response = train_model(data)
print("Model training completed.")
print(model_response)