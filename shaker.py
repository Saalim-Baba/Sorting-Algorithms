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


def shakersort_int(data: list, pos_count: int):
    datalength = len(data) - 1
    for iteration in range(datalength):
        for element in range(datalength - iteration):

            if data[element][pos_count] > data[element + 1][pos_count]:
                data[element], data[element + 1] = data[element + 1], data[element]
            else:
                continue

    return data


start_time = time.time()
sorted_data = shakersort_int(load_data(), 0)
end_time = time.time()

for entry in sorted_data:
    print(entry)

print(f"Time taken: {end_time - start_time} seconds")
