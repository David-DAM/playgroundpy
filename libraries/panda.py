import pandas as pd


def simple_data():
    dataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }

    df = pd.DataFrame(dataset)

    print("Simple df")
    print(df)

    data_where = df.query("passings > 2")[['cars']]
    # data_where = df[df["passings"] > 2]
    # data_where = df.where(df["passings"] > 2, other="X")

    print("Data filtered")
    print(data_where)


def employee_data():
    df = pd.read_csv("../resources/employee_data.csv")

    higher_than_salary = df.query("salary > 10.000")[["first_name", "last_name", "salary", "location"]]
    max_salary = df.loc[df["salary"].idxmax()]
    print(max_salary)


if __name__ == "__main__":
    employee_data()
