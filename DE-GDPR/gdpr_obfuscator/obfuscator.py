import pandas as pd
from io import StringIO
from typing import List


def obfuscate_csv_data(csv_content: str, pii_fields: List[str]) -> bytes:
    if not isinstance(csv_content, str):
        raise TypeError("csv_content must be a raw string")

    df = pd.read_csv(StringIO(csv_content))

    for field in pii_fields:
        if field in df.columns:
            df[field] = "***"
        else:
            raise ValueError(f"Field '{field}' not found in CSV columns")

    return df.to_csv(index=False).encode("utf-8")
