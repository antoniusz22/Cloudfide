import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Regex for valid column name
    valid_col_pattern = re.compile(r'^[A-Za-z_]+$')

    #Validation of existing column names
    for col in df.columns:
        if not valid_col_pattern.fullmatch(col):
            return pd.DataFrame([])

    # Validation of new column name
    if not valid_col_pattern.fullmatch(new_column):
        return pd.DataFrame([])

    #Validation of operation characters
    allowed_chars_pattern = re.compile(r'^[A-Za-z_+\-*\s]+$')
    if not allowed_chars_pattern.fullmatch(role):
        return pd.DataFrame([])

    # Check unsupported operators
    if re.search(r'[\/%]', role) or '**' in role:
        return pd.DataFrame([])

    # Variables extraction from role and check they exist in df
    role_columns = re.findall(r'[A-Za-z_]+', role)
    if not all(col in df.columns for col in role_columns):
        return pd.DataFrame([])

    try:
        df_copy = df.copy()
        df_copy[new_column] = df_copy.eval(role)
        return df_copy
    except Exception:
        return pd.DataFrame([])
    
