import pytest
from gdpr_obfuscator.obfuscator import obfuscate_csv_data
import pandas as pd
from io import BytesIO


def test_obfuscate_csv_data_correct_fields():
    raw_csv = "id,name,email\n1,Alice,alice@example.com\n2,Bob,bob@example.com"
    pii_fields = ["name", "email"]

    obfuscated_bytes = obfuscate_csv_data(raw_csv, pii_fields)
    obfuscated_df = pd.read_csv(BytesIO(obfuscated_bytes))

    assert all(obfuscated_df["name"] == "***")
    assert all(obfuscated_df["email"] == "***")
    assert list(obfuscated_df["id"]) == [1, 2]


def test_obfuscate_csv_data_missing_field():
    raw_csv = "id,name,email\n1,Alice,alice@example.com"
    pii_fields = ["name", "phone"]

    with pytest.raises(ValueError) as exc_info:
        obfuscate_csv_data(raw_csv, pii_fields)

    assert "Field 'phone' not found" in str(exc_info.value)


def test_obfuscate_csv_data_invalid_input_type():
    invalid_input = {"name": "Alice", "email": "alice@example.com"}
    pii_fields = ["name"]

    with pytest.raises(TypeError) as exc_info:
        obfuscate_csv_data(invalid_input, pii_fields)

    assert "csv_content must be a raw string" in str(exc_info.value)
