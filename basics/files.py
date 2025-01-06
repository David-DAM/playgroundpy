def read(file):
    for line in file:
        print(line)


def write(file):
    file.write("\nHello, this is a file created with Python!")


def use_file(path, file_operation):
    try:
        with open(path, file_operation, encoding="utf-8") as file:

            match file_operation:
                case "r":
                    read(file)
                case "w":
                    write(file)
                case "a":
                    write(file)

    except FileNotFoundError:
        print("The file not exist")


if __name__ == "__main__":
    use_file("../resources/employee_data.csv", "r")
    # use_file("../resources/hello.txt", "w")
    # use_file("../resources/hello.txt", "a")
