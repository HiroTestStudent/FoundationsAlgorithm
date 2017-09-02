
# Array Sorting: Bubble Sort or Insertion Sort

class Program():
    def doSort_Bubblev1(array):

        x = 0

        while (x < len(array) - 1):

            y = x + 1

            while (y < len(array)):

                if (array[x] > array[y]):
                    temp = array[x]

                    array[x] = array[y]
                    array[y] = temp

                y = y + 1

            x = x + 1

        return array


    def doSort_Bubblev2(array):

        swapped = True

        while (swapped):

            swapped = False

            x = 0

            while (x < len(array) - 1):

                if (array[x] > array[x + 1]):
                    temp = array[x]

                    array[x] = array[x + 1]
                    array[x + 1] = temp
                    swapped = True

                x = x + 1

        return array

    def doSort_Insertion(array):

        for x in range(len(array)):

            value = array[x]
            j = x

            while (j > 0 and array[j - 1] > value):
                array[j] = array[j - 1]
                j = j - 1

            array[j] = value

        return array



array = [10, 12, 4, 18, 32, 3, 9]
print("BubbleV1 = ", Program.doSort_Bubblev1(array))
print("BubbleV2 = ", Program.doSort_Bubblev2(array))
print("Insertion = ", Program.doSort_Insertion(array))