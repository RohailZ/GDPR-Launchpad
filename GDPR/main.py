import json
from gdpr_obfuscator.obfuscator import obfuscate_csv_data
from gdpr_obfuscator.s3_handler import download_s3_file, upload_to_s3

config = {
    "file_to_obfuscate": "s3://your-bucket/input.csv",
    "pii_fields": ["name", "email"],
    "output_path": "s3://your-bucket/output.csv"
}

if __name__ == "__main__":
    csv_raw = download_s3_file(config["file_to_obfuscate"])
    obfuscated_data = obfuscate_csv_data(csv_raw, config["pii_fields"])
    upload_to_s3(config["output_path"], obfuscated_data)
    print("Obfuscation complete and file uploaded.")
