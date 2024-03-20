def load_data():
    subarray = []
    with open("SortSmall.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            subarray.append(entry.split(","))
        return subarray



print(load_data())

