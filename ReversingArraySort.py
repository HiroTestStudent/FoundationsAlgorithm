
# Reversing an Array

def doReverseArray(array):

    leftIndex = 0
    rightIndex = len(array) - 1

    while (leftIndex < rightIndex):

        temp = array[leftIndex]

        array[leftIndex] = array[rightIndex]
        array[rightIndex] = temp

        leftIndex = leftIndex + 1
        rightIndex = rightIndex - 1

    print(array)


array = [1,2,3,4,5,6]
doReverseArray(array)