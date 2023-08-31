import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees,employee_uni,on='id',how='left')
    # merged['unique_id'] = merged['unique_id'].fillna('null')
    return merged[['unique_id','name']]
