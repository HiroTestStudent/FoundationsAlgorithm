
def IsInArray(startElement, endElement, elementToFind,elements):
    index = (startElement + endElement) // 2
    while (startElement<=endElement):
        if (elements[index]== elementToFind):
            return "Found at the index of "+str(index)+" of the list"
            break
        elif (elementToFind > elements[index]):
            return IsInArray(index+1, endElement, elementToFind, elements)
        elif (elementToFind < elements[index]):
            return IsInArray(startElement, index-1, elementToFind, elements)
    else:
        return "Not Found in the list"

# Main:

numbers = [2,8,22,44,56,65,72,101,208,452,801]
print(IsInArray(0,len(numbers), 2, numbers))
print(IsInArray(0,len(numbers), 44, numbers))
print(IsInArray(0,len(numbers), 55, numbers))
