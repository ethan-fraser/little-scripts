import sys

a = sys.argv[1:]

for x in a:
    try:
        a[a.index(x)] = int(x)
    except ValueError:
        print("numbers only please")
        exit(1)

for index in range(len(a)):
    min_index = index

    for index2 in range(index+1, len(a)):
        if index != index2 and a[index2] < a[min_index]:
            min_index = index2

    if min_index != index:
        t = a[min_index]
        a[min_index] = a[index]
        a[index] = t

print(" ".join([str(i) for i in a]))