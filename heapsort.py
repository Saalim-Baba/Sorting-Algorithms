
import datetime
import time


def load_data():
    subarray = []
    with open("SortBig.txt", "r") as file:
        big_array = file.read().split("\n")
        for entry in big_array:
            entry = entry.split(",")
            subarray.append(entry)
            for i in subarray:
                try:
                    i[0] = int(i[0])
                    i[4] = int(i[4])
                    if isinstance(i[5], str):
                        i[5] = datetime.datetime(int(i[5].split(".")[2]), int(i[5].split(".")[1]),int(i[5].split(".")[0]))
                    i[6] = float(i[6])
                except ValueError:
                    continue
        return subarray


def Heapsort(array: list, sort_option: int):
    """

    Sort Options:
    (1) Nachname
    (2) PLZ
    (3) Geburtsdatum (dd.mm.yyyy)
    (4) Vermögen (Decimal)
    """

    options = [2, 4, 5, 6]
    option = options[sort_option - 1]

    n = len(array)

    def swap(x: int, y: int):
        _x, _y = array[x], array[y]
        array[y] = _x
        array[x] = _y

    def heapify(arr: list, i: int, heap_size: int):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < heap_size and arr[left][option] > arr[largest][option]:
            largest = left
        if right < heap_size and arr[right][option] > arr[largest][option]:
            largest = right

        if largest != i:
            swap(i, largest)
            heapify(arr, largest, heap_size)

    def build_max_heap(arr: list):
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, i, n)

    build_max_heap(array)
    for i in range(n - 1, 0, -1):
        swap(0, i)
        heapify(array, 0, i)


sigma = time.time()
Heapsort(load_data(), 1)
gamma = time.time()
print(gamma-sigma)
