import pandas as pd
students = pd.read_csv('students.csv')
scores = pd.read_csv('scores.csv')
print("Missing Values in Students")
print(students.isnull().sum())
students = students.dropna()
scores = scores.dropna()
merged_df = pd.merge(students, scores , on='student_id')
print("\nMerged Dataset Sample")
print(merged_df.head())
if 'score' in merged_df.columns:
    student_avg_scores = merged_df.groupby(['student_id', 'name'])['score'].mean().reset_index()
    student_avg_scores.rename(columns={'score': 'average_score'}, inplace=True)
else: 
    score_cols = merged_df.select_dtypes(include='number').columns
    merged_df['average_score']= merged_df[score_cols].mean(axis=1)
    student_avg_scores = merged_df[['student_id', 'name', 'average_score']]
print("\nStudent Average Score")
print(student_avg_scores.head())
top_5_students = student_avg_scores.sort_values(by='average_score', ascending=False).head(5)
print("Top 5 Students")
print(top_5_students)
avg_score_by_major = merged_df.groupby('major')['average_score'].mean()
print("\nAverage Score by Major ")
print(avg_score_by_major)