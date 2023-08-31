import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_count = employee.groupby('managerId').size().reset_index(name='report')
    result = report_count[report_count['report']>=5]
    
    df = result.merge(employee[['id','name']],left_on ='managerId' ,right_on ='id' ,how='inner')

    return df[['name']]