import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == "__main__":
    df = pd.read_csv("../resources/employee_data.csv")

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='location', y='age', data=df)

    plt.title('Distribution of age by location')
    plt.xlabel('Location')
    plt.ylabel('Age')

    plt.show()
