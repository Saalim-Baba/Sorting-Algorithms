import sys
import datetime
import time


def load_data(file_path="SortSmall.txt"):
    subarray = []
    try:
        with open(file_path, "r") as file:
            big_array = file.read().strip().split("\n")
            for entry in big_array:
                entry = entry.split(",")
                if len(entry) < 7:
                    continue
                try:
                    entry[0] = int(entry[0])
                    entry[4] = int(entry[4])
                    entry[5] = datetime.datetime.strptime(entry[5], "%d.%m.%Y")
                    entry[6] = float(entry[6])
                except ValueError:
                    continue
                subarray.append(entry)
        return subarray
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []


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
