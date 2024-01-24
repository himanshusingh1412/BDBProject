import numpy as np
import pandas as pd

def add_status_column(df):
    df['Status'] = np.where(df['GPA'] >= 3.5, 'High Achiever', 'Standard')
    return df

def filter_data(filtered_students):
    # Apply additional transformations to filtered_students
    filtered_students = add_status_column(filtered_students)

    # Display the DataFrame with additional 'Status' column
    print("\nDataFrame for Filtered Students with Additional Status Column:")
    return filtered_students
