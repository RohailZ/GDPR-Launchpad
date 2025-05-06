import pytest
from gdpr_obfuscator.obfuscator import obfuscate_csv_data

def test_obfuscate_csv_data():
    csv = "id,name,email\n1,John Smith,john@example.com\n2,Jane Doe,jane@example.com"
    pii_fields = ["name", "email"]
    result = obfuscate_csv_data(csv, pii_fields)
    obfuscated = result.decode("utf-8")

    assert "***" in obfuscated
    assert "John Smith" not in obfuscated
    assert "jane@example.com" not in obfuscated
