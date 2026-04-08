import pandas as pd
import matplotlib.pyplot as plt


def plot_subject_maximums(filename):
    df = pd.read_csv(filename)
    plt.plot(df.index, df['Math'])
    plt.plot(df.index, df['Science'])
    plt.plot(df.index, df['English'])
    plt.plot(df.index, df['Physics'])
    plt.plot(df.index, df['Chemistry'])

    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()  

    return len(df)
