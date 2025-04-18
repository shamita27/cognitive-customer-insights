from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("K_2BVUcIbeII5VP0q_Y0akOP6AWqp4By326mo-sGDyyt")
nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)

nlu.set_service_url("https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/bce14290-0477-44de-9c00-d5d659fa0e9a")

def analyze_sentiment(text):
    response = nlu.analyze(text=text, features=Features(sentiment=SentimentOptions())).get_result()
    return response["sentiment"]["document"]["label"]

print(analyze_sentiment("I am very happy with the service!"))