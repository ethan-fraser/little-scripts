import sys

def selection_sort(a):
    for index in range(len(a)):
        min_index = index

        for index2 in range(index+1, len(a)):
            if index != index2 and a[index2] < a[min_index]:
                min_index = index2

        if min_index != index:
            t = a[min_index]
            a[min_index] = a[index]
            a[index] = t

if __name__ == "__main__":
    fn = sys.argv[1]
    try:
        with open(fn, "r") as f:
            a = f.readlines()
    except IOError:
        print("File \"{fn}\" not found")
        exit(1)

    for x in a:
        try:
            a[a.index(x)] = int(x)
        except ValueError:
            print("numbers only please")
            exit(1)

    # a = [3, 4, 6, 3, 8, 12, 20]

    b = a[:]

    print(a)
    selection_sort(a)
    print(a)

    print(a == sorted(b))
