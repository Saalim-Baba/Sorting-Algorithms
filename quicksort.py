from datetime import *
from time import strptime


def load_data():
    subarray = []
    with open("SortSmall.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            entry = entry.split(",")
            subarray.append(entry)
            for i in subarray:
                i[0] = int(i[0])
                i[4] = int(i[4])
                i[6] = float(i[6])
                i[5] = strptime.i[5]
        return subarray


def quickSort(list):
    if not list:
        return list
    pivot = list[0]
    i = 4
    lesser = quickSort([check for check in list[1:] if check[i] < pivot[i]])
    greater = quickSort([check for check in list[1:] if check[i] >= pivot[i]])
    return lesser + [pivot] + greater


print(quickSort(load_data()))
