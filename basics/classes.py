class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person("David", 25)

    print(f"My name is {person.name}")
