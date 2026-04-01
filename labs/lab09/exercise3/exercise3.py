import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    data = pd.read_csv(filename)
    plt.plot(data.index, data['Math'])
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Scores Trends")
    plt.show()

    return len(data)

show_math_trend("labs/lab09/data/students.csv")