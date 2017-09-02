class HashTable():
    def __init__(self, tablesize):
        self.tablesize = tablesize

    def generateIndex(self, astring):
        index = 0

        for pos in range(len(astring)):
            index = index + ord(astring[pos])

        return index % self.tablesize

    def add(self, key):
        val = self.generateIndex(key)
        if self.tablesize[val] == None:
            self.tablesize[val] = key
        else:
            if type(self.tablesize[val]) == list:
                self.tablesize[val].append(key)
            else:
                self.tablesize[val] = [self.tablesize[val], key]

    def remove(self, key):
        val = self.generateIndex(key)
        while val < len(self.tablesize()) and key[val] is not None:
            if key[val] == key:
                self.tablesize[val] = None
                break

            val = val + 1

    def count(self, key):
        count = 0
        for i in key:
            if key[i] is not None:
                i = i + 1
            else:
                return count


    def __getitem__(self, key):
        return self.generateIndex(key)

    def __setitem__(self, key):
        self.add(key)


hash = HashTable(12)
print(hash.generateIndex("mom"))
print(hash.remove("mom"))
print(hash.count())

