import pandas as pd
df_students = pd.read_csv('students.csv')
df_students.columns = df_students.columns.str.lower()
print("FIRST 5 ROWS:")
print(df_students.head())
rows, cols = df_students.shape
print(f"Number of rows: {rows}, Number of columns: {cols}")
name_gpa= df_students[['name', 'gpa']]
print("\nName and GPA")
print(name_gpa.head())
high_gpa_students = df_students[df_students['gpa'] >= 3.5]
print("\nStudent with GPA >= 3.5")
print(high_gpa_students)
sorted_students = df_students.sort_values(by='gpa', ascending = False)
print("\nSorted by GPA")
print(sorted_students)
avg_gpa_by_major = df_students.groupby('major')['gpa'].mean()
print("\nAverage GPA by Major")
print(avg_gpa_by_major)