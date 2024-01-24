import pandas as pd
import numpy as np

def student_gen():
    np.random.seed(42)

    student_data = {
        'StudentID': range(1, 11),
        'Name': ['Student' + str(i) for i in range(1, 11)],
        'Age': np.random.randint(18, 25, size=10),
        'Grade': np.random.uniform(70, 100, size=10),
        'Department': ['Math', 'Physics', 'Chemistry', 'Biology', 'History',
                       'Computer Science', 'English', 'Geography', 'Economics', 'Art']
    }

    student_df = pd.DataFrame(student_data)
    print("student_df")
    return student_df
