import matplotlib.pyplot as plt
import pandas as pd


def salary_vs_age(dfr, plot):
    plot.figure(figsize=(8, 6))
    plot.scatter(dfr['age'], dfr['salary'], color='blue')
    plot.title('Salary vs Age')
    plot.xlabel('Age')
    plot.ylabel('Salary')
    plot.grid(True)
    plot.show()


def salary_histogram(dfr, plot):
    dfr['salary'].hist()
    plot.show()


def avg_salary_by_department(dfr, plot):
    avg_salary_by_dept = dfr.groupby('department')['salary'].mean()

    plot.figure(figsize=(8, 6))
    avg_salary_by_dept.plot(kind='bar', color='green')

    plot.title('Salary mean by department')
    plot.xlabel('Department')
    plot.ylabel('Salary mean')

    plot.xticks(rotation=45)
    plot.show()


if __name__ == "__main__":
    df = pd.read_csv("../resources/employee_data.csv")

    salary_vs_age(df, plt)
    # salary_histogram(df, plt)
    # avg_salary_by_department(df, plt)
