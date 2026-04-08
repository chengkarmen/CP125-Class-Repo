import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    average_math = data["Math"].mean()
    average_science = data["Science"].mean()
    average_english = data["English"].mean()
    means = [average_english, average_math, average_science]
    best_subject = ""
    if max(means) == average_science:
        best_subject = "Science"
    elif max(means) == average_english:
        best_subject = "English"
    elif max(means) == average_science:
        best_subject = "Science"
    
    worst_subject = ""
    if min(means) == average_science:
        worst_subject = "Science"
    elif min(means) == average_english:
        worst_subject = "English"
    elif min(means) == average_science:
        worst_subject = "Science"
    
    return {"Math": average_math,
            "Science": average_science,
            "English": average_english,
            "best_subject": best_subject,
            "worst_subject": worst_subject}

