import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(orders,company,on='com_id')
    red_mask = df[df['name']=='RED']['sales_id']
    result = sales_person[~sales_person['sales_id'].isin(red_mask)]
    return result[['name']]