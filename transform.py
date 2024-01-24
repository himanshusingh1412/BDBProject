import pandas as pd
import numpy as np

def add_gpa_column(df):
    print(df['Grade'])
    df['GPA'] = df['Grade'] / 20.0
    return df

def categorize_students_by_age(df):
    bins = [18, 20, 22, np.inf]
    labels = ['Young', 'Middle-aged', 'Senior']
    df['Age_Category'] = pd.cut(df['Age'], bins=bins, labels=labels)
    return df

def filter_students_by_department(df, department):
    filtered_df = df[df['Department'] == department]
    return filtered_df

def transform(student_df):
    student_df = add_gpa_column(student_df)
    student_df = categorize_students_by_age(student_df)
    filtered_students = filter_students_by_department(student_df, 'Computer Science')
    return filtered_students
