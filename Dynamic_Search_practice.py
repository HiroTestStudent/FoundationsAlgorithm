x = []
n = 10
for i in range(1, n):
    x.append(i) # you push your element here, as of now I have push i

print(x)

#URL: https://stackoverflow.com/questions/36812185/how-to-create-a-dynamic-list-in-python

from sys import getsizeof
def size(n):
    data = []
    for i in range(n):
        data.append(1)
        print('%s,%s' % (len(data), getsizeof(data)))

size(20)

#URL: https://www.r-bloggers.com/dynamic-arrays-in-r-python-and-julia/