import json
from gdpr_obfuscator.obfuscator import obfuscate_csv_data
from gdpr_obfuscator.s3_handler import download_s3_file, upload_to_s3


def lambda_handler(event, context):
    file_to_obfuscate = event["file_to_obfuscate"]
    pii_fields = event["pii_fields"]
    output_path = event["output_path"]

    csv_raw = download_s3_file(file_to_obfuscate)
    obfuscated_data = obfuscate_csv_data(csv_raw, pii_fields)
    upload_to_s3(output_path, obfuscated_data)

    return {
        "statusCode": 200,
        "body": json.dumps("Obfuscation complete and file uploaded."),
    }
