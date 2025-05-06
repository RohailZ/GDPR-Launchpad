import boto3

s3 = boto3.client("s3")

def download_s3_file(s3_path: str) -> str:
    bucket, key = s3_path.replace("s3://", "").split("/", 1)
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj["Body"].read().decode("utf-8")

def upload_to_s3(s3_path: str, data: bytes) -> None:
    bucket, key = s3_path.replace("s3://", "").split("/", 1)
    s3.put_object(Bucket=bucket, Key=key, Body=data)
