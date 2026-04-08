import pandas as pd


def explore_data(filename):
    data = pd.read_csv(filename)

    total_students = len(data)
    subjects = ["Math", "Science", "English"]
    math_average = float(data["Math"].mean())
    max = data["Math"].max()
    highest_math_student = list(data.loc[data["Math"] == max, "Name"])
    result = {"total_students": total_students,
              "subjects": subjects,
              "math_average": math_average,
              "highest_math_student": highest_math_student[0]}
    print(result)
    return result

result = explore_data("labs/lab09/data/students.csv")