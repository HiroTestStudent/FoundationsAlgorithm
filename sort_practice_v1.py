
#Bubble sort v1

def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                change = True
    return arr

#Bubble sort v2

def bubbleSort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp

#Bubble sort v3

def bSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a [j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a




































