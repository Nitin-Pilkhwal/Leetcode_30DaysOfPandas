import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_diff'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['emp_id','event_day'])['time_diff'].sum().reset_index()
    result.rename(columns={'event_day':'day','time_diff':'total_time'},inplace=True)
    return result