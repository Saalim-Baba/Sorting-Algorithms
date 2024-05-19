from datetime import datetime
import time


def load_data():
    subarray = []
    with open("SortSmall.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            entry = entry.split(",")
            if len(entry) >= 7:
                try:
                    entry[0] = int(entry[0])
                    entry[4] = int(entry[4])
                    if isinstance(entry[5], str):
                        entry[5] = datetime.strptime(entry[5], "%d.%m.%Y")
                    entry[6] = float(entry[6])
                    subarray.append(entry)
                except ValueError:
                    continue
    return subarray


def bubblesort(data: list, pos_count: int):
    """Sort the array by using bubblesort."""

    datalength = len(data) - 1
    for iteration in range(datalength):
        for element in range(datalength - iteration):

            if data[element][pos_count] > data[element + 1][pos_count]:
                data[element], data[element + 1] = data[element + 1], data[element]
            else:
                continue

    return data


start_time = time.time()
sorted_data = bubblesort(load_data(), 0)
end_time = time.time()

for entry in sorted_data:
    print(entry)

print(f"Time taken: {end_time - start_time} seconds")
