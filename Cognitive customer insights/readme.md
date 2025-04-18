# Customer Segmentation & Analytics with IBM Watson AI

## Overview

This project leverages IBM Watson Natural Language Understanding (NLU), IBM Cloud Object Storage, and Watsonx.ai to perform customer segmentation and analytics. It automates sentiment analysis, categorization, and insights extraction for enhanced customer engagement.

## Features

- Automated Customer Segmentation using Watsonx.ai
- Sentiment & Intent Analysis powered by Watson NLU
- Data Storage & Retrieval with IBM Cloud Object Storage
- Streamlit Dashboard for visualization

## Prerequisites

1. IBM Cloud Account - Create an account on [IBM Cloud](https://cloud.ibm.com/).
2. IBM Watson Services - Enable Watson NLU and Watsonx.ai.
3. IBM Cloud Object Storage - Set up a storage bucket for dataset handling.
4. Python Environment - Install Python 3.8+.

## Installation

Clone the repository and install dependencies:
bash
$ git clone https://github.com/your-repo/your-project.git
$ cd your-project
$ pip install -r requirements.txt

## Configuration

1. IBM Watson Credentials: Obtain API keys for Watson NLU & Watsonx.ai from IBM Cloud.
2. Cloud Object Storage Config: Set up IBM COS credentials for dataset access.
3. Environment Variables:
   - Create a .env file with:

     IBM_NLU_API_KEY=<your-api-key>
     IBM_WATSONX_API_KEY=<your-api-key>
     IBM_COS_ENDPOINT=<your-storage-endpoint>
     IBM_COS_BUCKET=<your-bucket-name>

## Usage

Run the Streamlit application:
bash
$ streamlit run app.py

## Output

- _Customer Segmentation Analysis_
- _Sentiment Breakdown & Intent Detection_
- _Engagement Recommendations_

## Deployment

To deploy on IBM Cloud, use:
bash
$ ibmcloud app push

## License

This project is licensed under the MIT License.
