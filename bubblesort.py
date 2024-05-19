from datetime import datetime


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



def bubblesort_int(data: list, pos_count: int):
    datalength = len(data) - 1
    for iteration in range(datalength):
        for element in range(datalength - iteration):

            if data[element][pos_count] > data[element + 1][pos_count]:
                data[element], data[element + 1] = data[element + 1], data[element]
            else:
                continue

    return data


print(bubblesort_int(load_data(), 0))
