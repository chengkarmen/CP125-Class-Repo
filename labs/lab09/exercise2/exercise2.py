import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    average_math = data["Math"].mean()
    average_science = data["Science"].mean()
    average_english = data["English"].mean()