import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grp = courses.groupby(['class'])['student'].count().reset_index()
    result = grp[grp['student']>=5]
    return result[['class']]