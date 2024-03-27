def load_data(filepath:str):
    subarray = []
    with open(filepath, "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            subarray.append(entry.split(","))
        return subarray

def quicksort(subarray):



print(load_data())
