import math


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
    with open("20-nums") as f:
        a = f.readlines()
    a = [int(x.strip()) for x in a]

    # a = [3, 4, 6, 3, 8, 12, 20]

    b = a[:]

    print(a)
    heapSort(a)
    print(a)

    print(a == sorted(b))

