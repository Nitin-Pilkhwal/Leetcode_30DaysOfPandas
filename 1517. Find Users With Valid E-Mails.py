import pandas as pd
import re
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$'
    valid_emails_df = users[users['mail'].str.match(pattern)]
    return valid_emails_df