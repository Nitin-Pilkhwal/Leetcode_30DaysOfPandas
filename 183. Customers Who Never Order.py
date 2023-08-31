import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns={'name':'Customers'},inplace=True)
    mask = customers[~customers['id'].isin(orders['customerId'])]
    # mask_df = customers[~customers['id'].isin(orders['customersId'])]
    return mask[['Customers']]