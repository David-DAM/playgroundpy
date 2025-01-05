if __name__ == "__main__":
    try:
        with open("../resources/employee_data.csv", "r") as file:
            for line in file:
                print(line)

    except FileNotFoundError:
        print("The file not exist")
