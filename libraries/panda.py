import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


def simple_data():
    dataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }

    dfr = pd.DataFrame(dataset)

    print("Simple df")
    print(dfr)

    data_where = dfr.query("passings > 2")[['cars']]
    # data_where = df[df["passings"] > 2]
    # data_where = df.where(df["passings"] > 2, other="X")

    return data_where


def employee_max_salary(df: DataFrame):
    return df.loc[df["salary"].idxmax()]


def employee_greater_salary(df: DataFrame):
    return df.query("salary > 10.000")[["first_name", "last_name", "salary", "location"]]


def employee_full_name(df):
    return df["first_name"].str.cat(df["last_name"], sep=" ")


def employee_greater_salary_by_location(df: DataFrame):
    return df.groupby("location").apply(lambda group: group.loc[group['salary'].idxmax()])


def change_date_format(df: DataFrame):
    df['hire_date'] = pd.to_datetime(df['hire_date'])
    return df['hire_date'].dt.strftime('%d/%m/%Y')


if __name__ == "__main__":
    df = pd.read_csv("../resources/employee_data.csv")

    # data = simple_data()
    # higher_than_salary = employee_greater_salary(df)
    # max_salary = employee_max_salary(df)
    # df["full_name"] = employee_full_name(df)
    # top_employee_by_city = employee_greater_salary_by_location(df)
    # df['hire_date'] = change_date_format(df)

    # print(df.describe())
    print(df.head())
