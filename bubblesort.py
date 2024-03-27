import datetime


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
