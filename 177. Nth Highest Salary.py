import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates()
    salary.sort_values(ascending=False,inplace = True)
    if N>len(salary):
        return pd.DataFrame({'getNthHighestSalary':[None]})
    return pd.DataFrame({'getNthHighestSalary':[salary.iloc[N-1]]})
