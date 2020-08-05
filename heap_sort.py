import math
import sys

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def heapify(array, end, root):
    largest = root
    leftChild = root*2+1
    rightChild = root*2+2

    if leftChild < end and array[leftChild] > array[largest]:
        largest = leftChild
    if rightChild < end and array[rightChild] > array[largest]:
        largest = rightChild

    if largest != root:
        swap(array, root, largest)
        heapify(array, end, largest)


def buildHeapA(array, end):
    start = 1
    while start < end:
        for i in range(start):
            heapify(array, end, i)
        start += 1


def buildHeapB(array, end):
    start = math.floor(end/2)-1
    for i in range(start, -1, -1):
        heapify(array, end, i)


def heapSort(array):
    end = len(array)
    #organise elements into heap
    buildHeapB(array, end)
    while end > 1:
        #exchange first and last element, exclude last from the rest
        end -= 1
        swap(array, 0, end)
        #reorganise elements into heap
        buildHeapB(array, end)


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
    heapSort(a)
    print(a)

    print(a == sorted(b))

