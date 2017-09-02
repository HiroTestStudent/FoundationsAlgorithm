
# Bubble Sorting

def doBubbleSortv1(array):

    x = 0

    while (x < len(array) - 1):

        y = x + 1

        while (y < len(array)):

            if(array[x] > array[y]):

                temp = array[x]

                array[x] = array[y]
                array[y] = temp

            y = y + 1

        x = x + 1

    return array

array = [10, 12, 4, 18, 32, 3, 9]
print(doBubbleSortv1(array))


