
#Parsing Integer to String

def IntToString(value):
    output = ""
    if(value < 0):
        output = output + "-"
        value = -value
    factor = 1
    while ((value/factor) > 10):
        factor = factor * 10
        while (factor >= 1):
            digit = int(value/factor)
            output = output + str(digit)
            value = value - (int(digit)*factor)
            factor = factor/10
    return output

results = IntToString(-1023)
print("-1023 to string = {} and type = {}".format(results, type(results)))
