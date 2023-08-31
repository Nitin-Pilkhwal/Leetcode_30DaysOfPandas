import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    text = r"\bDIAB1"
    return patients[patients['conditions'].str.contains(text,case=False)]