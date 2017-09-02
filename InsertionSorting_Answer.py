#!/usr/bin/env python

'''
requires:
python3
'''

def doSort(array):
    counter = 1
    for x in array[1:]:
        el = x

        j = counter

        while j > 0 and array[j - 1] > el:
            array[j] = array[j - 1]
            j = j - 1

        array[j] = el

        counter += 1

def main():
    my_array = [10, 12, 4, 18, 32, 3, 9]

    for x in my_array:
        print(x)

    doSort(my_array)

    for x in my_array:
        print(x)

if __name__ == "__main__":
    main()