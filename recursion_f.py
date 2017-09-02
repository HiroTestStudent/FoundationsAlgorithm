#def Fib(fib):
    #return 0

#print("Fib(7) = {}".format(Fib(7)))

def fibonacci(n, a=1, b=0):
    return b if n < 1 else fibonacci(n - 1, a + b, a)

print(fibonacci(7))


#class Program():

    #def Fib(fib):
        #if fib == 0:
            #return 0
        #elif fib == 1:
            #return 1
        #else:
            #return Fib(fib - 1 ) + Fib(fib - 2)

#print(Program.Fib(7))

def fib(n):
    if n<2:
        return n
    else:
         return fib(n -1) + fib(n-2)
print(fib(7))