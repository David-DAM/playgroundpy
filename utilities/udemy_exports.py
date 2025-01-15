import pandas as pd

if __name__ == "__main__":

    date_from = "2025-01-06"
    date_to = "21-17-28"

    print("""
        Select some of the actions:
        1.Get report from reviews
        2.Get student list
        3.Exit
    """)

    action = int(input())

    file_path = ""

    while action != 3:
        match action:
            case 1:
                file_path = f"../resources/Udemy_Reviews_Export_{date_from}_{date_to}.csv"
            case 2:
                file_path = f"../resources/Students_List_Export_{date_from}_{date_to}.csv"
            case 3:
                exit(1)
            case _:
                print("Data does not match any specific condition")

    df = pd.read_csv(file_path)

    print(df.describe())
