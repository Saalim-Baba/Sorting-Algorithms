import sys
import datetime
import time


def load_data():
    subarray = []
    with open("SortSmall.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            entry = entry.split(",")
            subarray.append(entry)
            for i in subarray:
                try:
                    i[0] = int(i[0])
                    i[4] = int(i[4])
                    if isinstance(i[5], str):
                        i[5] = datetime.datetime(int(i[5].split(".")[2]), int(i[5].split(".")[1]),
                                                 int(i[5].split(".")[0]))
                    i[6] = float(i[6])
                except ValueError:
                    continue
        return subarray


def sort(array, sort_option: int):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        i = sort_option
        for x in array:
            if x[i] < pivot[i]:
                less.append(x)
            elif x[i] == pivot[i]:
                equal.append(x)
            elif x[i] > pivot[i]:
                greater.append(x)
        return sort(less, sort_option) + equal + sort(greater, sort_option)
    else:
        return array


start_time = time.time()
sorted_data = sort(load_data(), 1)
end_time = time.time()

for entry in sorted_data:
    print(entry)

print(f"Time taken: {end_time - start_time} seconds")
