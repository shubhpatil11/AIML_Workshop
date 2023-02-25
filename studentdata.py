# -*- coding: utf-8 -*-
"""StudentData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13D_4pAAzCAxJEUcND_xGpI6Dt9yVJWO-
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

np.random.seed(0)
n_students = 100
marks_obtained = np.random.randint(0,100,n_students)
attendance_percentage = np.random.randint(50,100,n_students)
assignments_score = np.random.randint(0,10,n_students)

overall_score = marks_obtained*0.4 + attendance_percentage*0.4 + assignments_score*0.2

data = pd.DataFrame({
    "Marks Obtained" : marks_obtained,
    "Attendance Percentage" : attendance_percentage,
    "Assignments Score" : assignments_score,
    "Overall Score" : overall_score,
})

data["cluster"] = np.where(data["Overall Score"]<40, 0, np.where(data["Overall Score"]<75, 1, 2))

new_data = pd.DataFrame({
    "Marks Obtained" : [10],
    "Attendance Percentage" : [35],
    "Assignments Score" : [8],
})

New_Student_Overall_Score = new_data["Marks Obtained"]*0.4 + new_data['Attendance Percentage']*0.4 + new_data["Assignments Score"]*0.2

new_student_cluster = np.where(New_Student_Overall_Score<40, 0, np.where(New_Student_Overall_Score<75, 1, 2))

print("The overall score of new student is : ",New_Student_Overall_Score)
print("New Student Belongs to the Cluster : ",new_student_cluster[0])