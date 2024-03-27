
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
                    i[6] = float(i[6])
                except ValueError:
                    continue
        return subarray


def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        i = 6
        for x in array:
            if x[i] < pivot[i]:
                less.append(x)
            elif x[i] == pivot[i]:
                equal.append(x)
            elif x[i] > pivot[i]:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array


print(sort(load_data()))
