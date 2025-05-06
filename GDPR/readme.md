## GDPR Obfuscator (Student Project)
This is a simple Python project that helps hide personal information (like names and emails) from CSV files stored in Amazon S3. It’s useful for practicing how to handle data privacy in cloud-based systems — especially when learning about GDPR (General Data Protection Regulation).

# What It Does
This tool:

Downloads a CSV file from S3
Replaces sensitive information (PII) like names and emails with ***
Uploads the cleaned CSV back to S3

# Project Files

gdpr_obfuscator/
├── main.py           # Main script to run everything
├── obfuscator.py     # Handles the obfuscation logic
└── s3_handler.py     # Deals with downloading and uploading files to S3

# Requirements
Make sure you have:

Python 3.8 or later
An AWS account and credentials set up (e.g. via ~/.aws/credentials)
These Python packages installed:

pip install pandas boto3

# How to Use
Open main.py and set the configuration like this:

config = {
    "file_to_obfuscate": "s3://your-bucket/input.csv",
    "pii_fields": ["name", "email"],  # Columns you want to hide
    "output_path": "s3://your-bucket/output.csv"
}

Then just run:

python main.py

That’s it! 
It will:

Download the CSV from S3
Obfuscate the fields you picked
Upload the cleaned version back to S3

# Example
Input CSV (before):

name,email,age
John Doe,john@example.com,28
Jane Smith,jane@example.com,31

Output CSV (after):

name,email,age
***,***,28
***,***,31

# What You’ll Learn
How to read and write CSV files with pandas
How to work with AWS S3 using boto3
Basic data privacy concepts like PII obfuscation
Structuring a small Python project

# Notes
Make sure the column names in pii_fields match your CSV exactly.
