import json
import ibm_boto3
from ibm_botocore.client import Config

# Load credentials
with open("config/ibm_credentials.json") as f:
    creds = json.load(f)

# Initialize IBM Cloud Object Storage client
cos_client = ibm_boto3.client(
    "s3",
    ibm_api_key_id=creds["COS_API_KEY"],
    ibm_service_instance_id=creds["COS_INSTANCE_CRN"],
    config=Config(signature_version="oauth"),
    endpoint_url=creds["COS_ENDPOINT"]
)

# Function to upload dataset
def upload_to_cos(file_path, bucket_name, object_name):
    with open(file_path, "rb") as file:
        cos_client.upload_fileobj(file, bucket_name, object_name)
    print(f"Uploaded {object_name} to IBM Cloud Storage.")

# Upload dataset
upload_to_cos("data/customer_reviews.csv", creds["COS_BUCKET_NAME"], "customer_reviews.csv")