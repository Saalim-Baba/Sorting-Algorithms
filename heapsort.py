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


def Heapsort(array: list, sort_option: int):
    option_index_map = {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6
    }
    option = option_index_map.get(sort_option, 0)  # Default to sorting by ID if invalid option

    def swap(x: int, y: int):
        array[x], array[y] = array[y], array[x]

    def heapify(arr: list, n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left][option] > arr[largest][option]:
            largest = left

        if right < n and arr[right][option] > arr[largest][option]:
            largest = right

        if largest != i:
            swap(i, largest)
            heapify(arr, n, largest)

    def build_max_heap(arr: list):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

    n = len(array)
    build_max_heap(array)
    for i in range(n - 1, 0, -1):
        swap(0, i)
        heapify(array, i, 0)

    return array


start_time = time.time()
sorted_data = Heapsort(load_data(), 0)
end_time = time.time()
for entry in sorted_data:
    print(entry)

print(f"Time taken: {end_time - start_time} seconds")
