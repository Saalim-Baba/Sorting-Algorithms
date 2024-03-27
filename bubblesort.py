
from datetime import datetime



def load_data():
    subarray = []
    with open("SortMedium.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            entry = entry.split(",")
            subarray.append(entry)
            for i in subarray:
                try:
                    i[0] = int(i[0])
                    i[4] = int(i[4])
                    if isinstance(i[5], str):



def bubblesort_int(data: list, pos_count: int):
    datalength = len(data)-1
    for iteration in range(datalength):
        for element in range(datalength-iteration):

            if data[element][pos_count] > data[element+1][pos_count]:
                data[element], data[element + 1] = data[element + 1], data[element]
            else:
                continue

    return data

print(bubblesort_int(load_data(), 4))


