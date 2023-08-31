import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_count = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']].size
    immediate_perc = round((immediate_count/delivery.size)*100,2)
    return pd.DataFrame({'immediate_percentage':[immediate_perc]})