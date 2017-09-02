#!/usr/bin/env python

'''
requires:
python3
'''

import numpy as np  # for creating arrays


# import sys # for getting this size of an object

class dynArray():
    def __init__(self, index, initialSize=3):
        self.index = index
        self.initialSize = initialSize
        self.dynArray = np.empty(initialSize, dtype=int)

    def get_length(self):
        return len(self.dynArray)

    def check_index(self):
        if self.index >= self.get_length():
            raise SystemExit("Index out of range.")
        else:
            return self.index

    def add_to(self, num):
        if self.check_index():
            self.index += 1 # self.index = self.index + 1
            self.dynArray = np.insert(self.dynArray, self.index, num) # np = numpy
            return self.dynArray
        else:
            self.resize(self.get_length() + self.initialSize)
            self.index += 1 # self.index = self.index + 1
            self.dynArray = np.insert(self.dynArray, self.index, num) # np = numpy
            return self.dynArray

    def resize(self, resize):
        self.dynArray = np.resize(self.dynArray, resize) # np = numpy
        return self.dynArray


def main():
    myArray = dynArray(0)

    myArray.resize(7)

    print(myArray.index)
    print(myArray.get_length())

    myArray.add_to(6)
    myArray.add_to(12)

    print(myArray.get_length())


if __name__ == "__main__":
    main()