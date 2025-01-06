import queue
from array import array
from collections import deque, Counter


# Collections ordered with mutable data, can contain different types of data
def lists():
    data = [1, 2, 3, 4, 5, "David"]

    data.remove(5)
    print(f"List with element removed: {data}")

    data.append(5)

    for datum in data:
        print(f"Number {datum}")

    print(f"List sliced: {data[1:3]}")
    print(f"List reversed: {data[::-1]}")


# Collections ordered with immutable data, can contain different types of data
def tuples():
    data = (24, "David", 20, "Alberto")
    print(f"Tuples {data}")

    print(f"First element: {data[0]}")


# Collections unordered with immutable data, can contain different types of data
def sets():
    data = {1, 2, 3, 4, 5, 6}
    data2 = {1, 2, 3, 4, 5}
    print(f"Set of data: {data}")

    intersection = data.intersection(data2)
    union = data.union(data2)
    difference = data.difference(data2)

    print(f"Intersection {intersection}")
    print(f"Union {union}")
    print(f"Difference {difference}")


# Collections of key-value
def dictionaries():
    data = {"David": 25, "Alberto": 20}
    data["John"] = 80
    data.pop("Alberto")
    print(f"Data {data}")
    print(f"Data for David {data["David"]}")


def strings():
    data = "Hello world!"

    print(f"Data {data}")

    replace = data.replace("world", "David")

    print(f"Data replaced {replace}")


def collections():
    my_deque = deque([1, 2, 3])
    my_deque.popleft()

    my_counter = Counter(['apple', 'banana', 'apple'])
    most_common = my_counter.most_common()

    print(f"Data queue {my_deque}")
    print(f"Data counter items {my_counter}")
    print(f"Data counter most common {most_common}")


def arrays():
    my_array = array('i', [1, 2, 3, 4])
    print(f"Data  {my_array}")
    print(f"First data  {my_array[0]}")


def queues():
    my_queue = queue.Queue()
    my_queue.put(1)
    my_queue.put(2)

    print(f"First Data  {my_queue.get()}")


def manipulate_list():
    names = ["david", "alberto", "john"]

    mapped = [name.upper() for name in names]

    filtered = [name for name in mapped if name.startswith("D")]

    print(filtered)


def manipulate_list2():
    names = ["david", "alberto", "john"]

    mapped = list(map(lambda name: name.upper(), names))

    filtered = list(filter(lambda name: name.startswith("D"), mapped))

    print(filtered)


if __name__ == '__main__':
    # lists()
    manipulate_list()
