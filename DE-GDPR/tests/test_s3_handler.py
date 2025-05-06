import boto3
import os
from moto import mock_aws
import pytest
from gdpr_obfuscator.s3_handler import download_s3_file


@pytest.fixture()
def aws_creds():
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.fixture()
def s3_client(aws_creds):
    with mock_aws():
        mock_s3 = boto3.client("s3", region_name="eu-west-2")
        yield mock_s3

@mock_aws
def test_download_s3_file(s3_client):
    bucket = "test-bucket"
    key = "test.csv"
    csv_content = "name,email\nJohn,john@example.com"

    s3_client.create_bucket(Bucket=bucket, CreateBucketConfiguration={"LocationConstraint": "eu-west-2"})
    s3_client.put_object(Bucket=bucket, Key=key, Body=csv_content)

    data = download_s3_file(f"s3://{bucket}/{key}")
    assert "John" in data 
