import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income']<20000]['income'].count()
    average = accounts[(accounts['income']>=20000) & (accounts['income']<=50000)]['income'].count()
    high = accounts[accounts['income']>50000]['income'].count()
    df = pd.DataFrame({'category':['Low Salary','Average Salary','High Salary'],'accounts_count':[low,average,high]})
    return df