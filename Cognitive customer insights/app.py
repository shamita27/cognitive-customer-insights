import streamlit as st
import pandas as pd
import json
import requests

# Load credentials
with open("config/ibm_credentials.json") as f:
    creds = json.load(f)

# Watson NLU API details
NLU_URL = creds["NLU_URL"]
NLU_API_KEY = creds["NLU_API_KEY"]

# Streamlit UI
st.title("📊 Cognitive Customer Insights with Watson AI")

# Upload CSV File
uploaded_file = st.file_uploader("Upload Customer Reviews CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Dataset:")
    st.dataframe(df)

    # Perform Sentiment Analysis
    def analyze_text(text):
        response = requests.post(
            f"{NLU_URL}/v1/analyze?version=2021-08-01",
            json={"text": text, "features": {"sentiment": {}}},
            headers={"Authorization": f"Bearer {NLU_API_KEY}"}
        )
        return response.json().get("sentiment", {}).get("document", {}).get("label", "Unknown")

    if st.button("Analyze Sentiments"):
        df["Sentiment"] = df["Review"].apply(lambda x: analyze_text(x))
        st.write("### Sentiment Analysis Results:")
        st.dataframe(df)

st.write("Developed using IBM Cloud Services & Watson AI")