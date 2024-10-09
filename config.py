import os

# AWS Configuration
S3_BUCKET = os.getenv("S3_BUCKET", "test-commvault-10924")
S3_REGION = os.getenv("S3_REGION", "eu-north-1")
