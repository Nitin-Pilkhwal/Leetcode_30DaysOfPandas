import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    left = pd.merge(students,subjects,how='cross').sort_values(by=['student_id','subject_name'])
    right = examinations.groupby(['student_id','subject_name']).agg(attended_exams=('subject_name','count')).reset_index()
    df = pd.merge(left,right,on=['student_id', 'subject_name'],how='left').fillna(0)
    return df[['student_id', 'student_name', 'subject_name', 'attended_exams']]