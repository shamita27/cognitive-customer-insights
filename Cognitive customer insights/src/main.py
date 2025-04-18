import json
import pandas as pd
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from config import NLU_API_KEY, NLU_URL
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate Watson NLU
authenticator = IAMAuthenticator(NLU_API_KEY)
nlu = NaturalLanguageUnderstandingV1(version="2022-04-07", authenticator=authenticator)
nlu.set_service_url(NLU_URL)

# Load dataset
df = pd.read_csv("../data/customer_reviews.csv")

# Analyze sentiment
results = []
for review in df["review"]:
    response = nlu.analyze(text=review, features=Features(sentiment=SentimentOptions())).get_result()
    sentiment = response["sentiment"]["document"]
    results.append({"review": review, "sentiment": sentiment["label"], "score": sentiment["score"]})

# Save analysis results
with open("../outputs/analysis_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Sentiment analysis complete! Results saved.")