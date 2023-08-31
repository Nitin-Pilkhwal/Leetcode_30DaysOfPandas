import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates()
    salary.sort_values(ascending = False,inplace=True)
    if len(salary)<2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    return pd.DataFrame({'SecondHighestSalary':[salary.iloc[1]]})

