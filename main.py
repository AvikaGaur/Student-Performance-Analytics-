
import pandas as pd
import numpy as np
from functions import total_marks, average_marks, grade, result

data = pd.read_csv("students.csv")

print("Student Performance Analytics System")
print(data)

totals = []
averages = []
grades = []
results = []

for i in range(len(data)):
    marks = [data.loc[i, "Python"], data.loc[i, "Maths"], data.loc[i, "English"]]

    total = total_marks(marks)
    avg = average_marks(marks)

    totals.append(total)
    averages.append(avg)
    grades.append(grade(avg))
    results.append(result(marks))

data["Total"] = totals
data["Average"] = averages
data["Grade"] = grades
data["Result"] = results

print("\nStudent Results")
print(data[["Name", "Total", "Average", "Grade", "Result"]])

print("\nClass Average:", round(np.mean(averages), 2))
print("Highest Average:", max(averages))
print("Lowest Average:", min(averages))

print("\nSubject Averages")
print("Python:", round(data["Python"].mean(), 2))
print("Maths:", round(data["Maths"].mean(), 2))
print("English:", round(data["English"].mean(), 2))

passed = 0
failed = 0

for r in results:
    if r == "Pass":
        passed = passed + 1
    else:
        failed = failed + 1

print("\nPassed Students:", passed)
print("Failed Students:", failed)

top = data["Average"].idxmax()
print("Top Student:", data.loc[top, "Name"])

data.to_csv("final_result.csv", index=False)
