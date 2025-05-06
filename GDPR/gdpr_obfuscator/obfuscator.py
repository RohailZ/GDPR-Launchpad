import pandas as pd
from io import StringIO

def obfuscate_csv_data(csv_content: str, pii_fields: list[str]) -> bytes:
    df = pd.read_csv(StringIO(csv_content))
    for field in pii_fields:
        if field in df.columns:
            df[field] = '***'
    output = StringIO()
    df.to_csv(output, index=False)
    return output.getvalue().encode("utf-8")
