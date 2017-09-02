
# set lab

class Set():
    # Creates an empty set instance
    def __init__(self):
        self.Elements = list()

    # Returns the number of items in the set
    def __len__(self):
        return len(self.Elements)

    # Adds a new unique element to the set.
    def Add(self, element):
        if element not in self:
            self.Elements.append(element)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True


# create first set
set = Set()
set.Add(2)
set.Add(4)
set.Add(3)
set.Add(2)

# create second set
set2 = Set()
set2.Add(2)
set2.Add(3)

# check if the second set is a subset of the first
