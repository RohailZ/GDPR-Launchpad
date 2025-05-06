# GDPR Data Obfuscator

A simple Python tool that helps anonymize personal data in CSV files.  
This project reads data from AWS S3, removes/masks personally identifiable information (PII), and puts the clean data back in S3.  
Perfect for class projects dealing with GDPR compliance!

---

## What it does

- Takes CSVs with personal data from S3  
- Anonymizes fields containing personal info (emails, names, etc.)  
- Saves the clean data back to S3  
- Runs as an AWS Lambda function  
- Deploys automatically with GitHub Actions  

---

## Project Structure

dimensional-transformers-project/
├── gdpr_obfuscator/ # The main code
├── tests/ # Test files
├── terraform/ # AWS deployment stuff
├── .github/workflows/ # CI/CD pipeline
└── various config files...


## Getting Started 🚀

### Set up your environment

# Create virtual environment and install dependencies
make create-environment
source venv/bin/activate
make dev-setup

# Run all the checks and tests
make run-checks

# Use it locally

from gdpr_obfuscator.obfuscator import obfuscate_csv
from gdpr_obfuscator.s3_handler import download_from_s3, upload_to_s3

# Get data from S3
csv_file = download_from_s3('my-bucket', 'data.csv', '/tmp/data.csv')

# Anonymize it
obfuscated_file = obfuscate_csv(csv_file, ['email', 'name', 'phone'])

# Save it back to S3
upload_to_s3('my-bucket', 'anonymized_data.csv', obfuscated_file)

# Deploy to AWS
Make sure you have AWS credentials set up, then:

cd terraform
terraform init
terraform apply

# GitHub Actions Setup
The project uses GitHub Actions to automatically test and deploy your code.
You'll need to add these secrets to your GitHub repo:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION

# Technical Bits
Uses hashing to anonymize data while keeping it usable for analysis
Handles CSV parsing with pandas
Written to be easy to extend with new anonymization methods
Has ~90% test coverage

# Need Help?
If you run into any issues:
Check the test failures for clues
Make sure your AWS permissions are set correctly
Reach out to me with questions